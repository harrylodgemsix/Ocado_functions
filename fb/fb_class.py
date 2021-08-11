import datetime
import json
import logging
import os
import sys
import uuid
from datetime import date, timedelta
from platform import version
from typing import ValuesView

import pandas as pd
import requests
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from google.cloud import bigquery, secretmanager, storage
from google.oauth2 import service_account
from googleapiclient import discovery, http
from pandas import json_normalize
from pandas.core.frame import DataFrame

import fields


def get_secret(project_id, secret_id):
    # gets latest secret

    client = secretmanager.SecretManagerServiceClient()
    request = {
        "name": f"projects/{project_id}/secrets/{secret_id}/versions/latest"}
    response = client.access_secret_version(request)
    secret_string = response.payload.data.decode("UTF-8")
    return secret_string


class fbConnectorForGCP():
    def __init__(
            self,
            ad_account,
            ad_account_name,
            access_token,
            app_id,
            app_secret,
            upload_bucket,
            project_id):
        self.ad_account = ad_account
        self.ad_account_name = ad_account_name
        self.access_token = access_token
        self.app_id = app_id
        self.app_secret = app_secret
        self.project_id = project_id
        self.all_campaign_ids = []
        self.active_campaign_ids = []
        self.df = None
        self.storage_bucket_name = upload_bucket

    def authenticate(self):
        FacebookAdsApi.init(self.app_id, self.app_secret, self.access_token)
        print("Authentication successful")

    def get_active_campaign_ids(self, date_list):
        self.start_date = date_list[0]
        self.end_date = date_list[-1]

        get_ids = AdAccount(self.ad_account).get_campaigns()
        for i in get_ids:
            data = dict(i)
            self.all_campaign_ids.append(data["id"])

        campaign_id_df = self.__call_api(
            "campaign", fields.FIELDS_FOR_CAMPAIGNS, self.all_campaign_ids)

        active_campaign_ids = pd.concat(campaign_id_df).reset_index(
            drop=True).campaign_id.to_list()

        # converts to set then back to list to remove duplicates
        self.unique_active_campaign_ids = list(set(active_campaign_ids))

        print("Get active campaign ids successful")

    def get_ad_data(self, date):
        self.date_to_query = date
        df_list = self.__call_api(
            "ad", fields.FIELDS_FOR_ADS, self.unique_active_campaign_ids)

        self.df = pd.concat(df_list).reset_index(
            drop=True)

    def transform(self):

        self.df = self.df.fillna(0)

        # splits out actions column metrics into seperate columns
        for index, action_type in enumerate(fields.ACTION_TYPE_LIST):
            value = self.__flatten_actions(self.df, action_type)
            value_series = pd.Series(value)
            self.df = pd.concat((self.df, value_series.rename(
                fields.NEW_COL_NAME[index])), axis=1)

        # if field not in df then add it in
        for k in fields.FIELDS + fields.NEW_COL_NAME:
            if k not in self.df:
                self.df[k] = 0

        print("Transform successful")

    def upload(self):

        self.storage_blob_name = f"fb/{self.ad_account_name}/{self.date_to_query}.csv"

        client = storage.Client()
        bucket = client.get_bucket(self.storage_bucket_name)
        blob = bucket.blob(self.storage_blob_name)

        df = self.df

        output = df.applymap(
            lambda x: x[0].get("value") if isinstance(
                x, list) is True and len(x) == 1 else x).fillna(0).to_csv(
            index=False)

        blob.upload_from_string(output)

        print("Data upload successful")

    def __call_api(self, granularity, fields_string, campaign_ids):

        if granularity == "campaign":
            params = (
                # to use time range instead of date present remove the comments
                # and comment in the date preset
                ('time_range[since]', self.start_date),
                ('time_range[until]', self.end_date),
                # ('date_preset', 'yesterday'),
                ('time_increment', '1'),
                ('level', granularity),
                ('fields', fields_string),
                ('access_token', self.access_token),
            )
        else:
            params = (
                # to use time range instead of date present remove the comments
                # and comment in the date preset
                ('time_range[since]', self.date_to_query),
                ('time_range[until]', self.date_to_query),
                # ('date_preset', 'yesterday'),
                ('time_increment', '1'),
                ('level', granularity),
                ('fields', fields_string),
                ('breakdowns', 'publisher_platform, platform_position, impression_device'),
                ('access_token', self.access_token),
                ('use_unified_attribution_setting', 'true'),
            )

        df = []
        try:
            for i in range(len(campaign_ids)):

                url = 'https://graph.facebook.com/v10.0/{}/insights'.format(
                    campaign_ids[i])
                response = requests.get(url, params=params)
                json_obj = json.loads(response.text)
                df.append(json_normalize(json_obj["data"]))

                try:
                    while ((json_obj["paging"] is not None) and (
                            json_obj["paging"]["next"] is not None)):
                        response = requests.get(json_obj["paging"]["next"])
                        json_obj = json.loads(response.text)
                        df.append(json_normalize(json_obj["data"]))
                except KeyError:
                    pass

        except Exception:
            print(json_obj)

        print("Api call successful")
        return df

    def __flatten_actions(self, df, action_type):

        value = []
        for action in df["actions"]:
            # if action row is 0 then append 0
            # df.fillna(0) should have been used before this
            if action == 0:
                value.append(0)

            # if there is not action type in i then append 0
            elif not any(i["action_type"] == action_type for i in action):
                value.append(0)

            # if action type in i then append i["value"]
            # if only 1d_view etc. is in dict then
            # append 0
            else:
                for i in action:
                    if i["action_type"] == action_type:
                        if i.get("value"):
                            value.append(i["value"])
                        else:
                            value.append(0)

        return value
