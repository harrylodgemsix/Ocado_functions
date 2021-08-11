import datetime
import os
import json
from datetime import date, timedelta

from fb_class import fbConnectorForGCP, get_secret

project_id = os.environ["project_id"]
upload_bucket = os.environ["upload_bucket"]

access_token = get_secret(project_id, "facebook_access_token")
app_id = get_secret(project_id, "facebook_app_id")
app_secret = get_secret(project_id, "facebook_app_secret")

dates_to_query = [date.today() - timedelta(days=2),
                  date.today() - timedelta(days=1)]


def facebook_api_call(request):
    request_json = request.get_json()

    ad_account_name = request_json["ad_account_name"]

    if "act_" in request_json["ad_account_id"]:
        ad_account_id = request_json["ad_account_id"]
    else:
        ad_account_id = "act_" + request_json["ad_account_id"]

    fb = fbConnectorForGCP(
        ad_account_id,
        ad_account_name,
        access_token,
        app_id,
        app_secret,
        upload_bucket,
        project_id)

    fb.authenticate()
    fb.get_active_campaign_ids(dates_to_query)

    for date in dates_to_query:
        fb.get_ad_data(date)
        fb.transform()
        fb.upload()

    return {"status": "success"}
