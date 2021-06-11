import datetime
import os
from datetime import date, timedelta

from fb_class import fbConnectorForGCP, get_secret

project_id = os.environ["project_id"]
upload_bucket = os.environ["upload_bucket"]

zoom_ad_account = get_secret(project_id, "facebook_ad_account_zoom")
supplier_activity_ad_account = get_secret(
    project_id, "facebook_ad_account_supplier_activity")
access_token = get_secret(project_id, "facebook_access_token")
app_id = get_secret(project_id, "facebook_app_id")
app_secret = get_secret(project_id, "facebook_app_secret")

dates_to_query = [date.today() - timedelta(days=2),
                  date.today() - timedelta(days=1)]


def facebook_api_call_zoom(request):
    for i in dates_to_query:
        fb = fbConnectorForGCP(i, zoom_ad_account, access_token, app_id, app_secret,
                               upload_bucket, "zoom", project_id)
        fb.run()

    return {"status": "success"}


def facebook_api_call_supplier_activity(request):
    for i in dates_to_query:
        fb = fbConnectorForGCP(i, supplier_activity_ad_account, access_token, app_id, app_secret,
                               upload_bucket, "supplier_activity", project_id)
        fb.run()

    return {"status": "success"}
