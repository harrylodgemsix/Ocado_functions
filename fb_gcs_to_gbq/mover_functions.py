import os
from re import L

import fsspec
import gcsfs
import pandas as pd
from google.cloud import bigquery, storage
from numpy.lib.utils import source


def fb_transform(bucket, folder, bigquery_import_table, project_id):
    df = get_df(bucket, folder)
    df = df[["account_name", "account_id", "date_start", "ad_name", "ad_id", "adset_name", "adset_id", "campaign_name", "campaign_id", "publisher_platform", "platform_position",
             "impressions", "clicks", "inline_link_clicks", "landing_page_views", "spend", "video_views_3_seconds", "video_p25_watched_actions", "video_p50_watched_actions",
             "video_p75_watched_actions", "video_p95_watched_actions", "video_p100_watched_actions"]]
    df.to_gbq(bigquery_import_table, project_id, if_exists="replace")


def fb_query(bigquery_import_table, bigquery_main_table):
    bq_client = bigquery.Client()
    query = f"""
        DELETE
        FROM
          {bigquery_main_table}
        WHERE
          date >= (DATE_ADD(CURRENT_DATE(), INTERVAL -2 DAY));
        INSERT INTO
          {bigquery_main_table}
        SELECT
          account_name,
          CAST(account_id AS string) AS account_id,
          CAST(date_start AS date) AS date,
          ad_name,
          CAST(ad_id AS string) AS ad_id,
          adset_name,
          CAST(adset_id AS string) AS adset_id,
          campaign_name,
          CAST(campaign_id AS string) AS campaign_id,
          publisher_platform,
          platform_position,
          SUM(CAST(impressions AS INT64)) AS impressions,
          SUM(CAST(clicks AS INT64)) AS clicks,
          SUM(CAST(inline_link_clicks AS INT64)) AS inline_link_clicks,
          SUM(CAST(landing_page_views AS INT64)) AS landing_page_views,
          SUM(CAST(spend AS FLOAT64)) AS spend,
          SUM(CAST(video_views_3_seconds AS INT64)) AS video_views_3_seconds,
          SUM(CAST(video_p25_watched_actions AS INT64)) AS video_p25_watched_actions,
          SUM(CAST(video_p50_watched_actions AS INT64)) AS video_p50_watched_actions,
          SUM(CAST(video_p75_watched_actions AS INT64)) AS video_p75_watched_actions,
          SUM(CAST(video_p95_watched_actions AS INT64)) AS video_p95_watched_actions,
          SUM(CAST(video_p100_watched_actions AS INT64)) AS video_p100_watched_actions,
        FROM
          {bigquery_import_table}
        GROUP BY
          account_name,
          account_id,
          date,
          ad_name,
          ad_id,
          adset_name,
          adset_id,
          campaign_name,
          campaign_id,
          publisher_platform,
          platform_position
    """
    bq_client.query(query)


def move_blob(bucket, new_bucket, blob_name):
    client = storage.Client()
    source_bucket = client.get_bucket(bucket)
    blobs_to_move = [blob for blob in source_bucket.list_blobs(
    ) if blob.name.startswith(blob_name)]
    newer_bucket = client.get_bucket(new_bucket)

    for blob in blobs_to_move:
        source_bucket.copy_blob(blob, newer_bucket, blob.name)
        blob.delete()


def get_df(bucket, blob_folder):
    client = storage.Client()
    df_list = []

    for blob in client.list_blobs(bucket, prefix=blob_folder):
        file_path = "gs://{}/{}".format(blob.bucket.name, blob.name)
        single_df = pd.read_csv(file_path)
        df_list.append(single_df)

    df = pd.concat(df_list).reset_index(drop=True)
    return df
