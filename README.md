Create 2 storage buckets:

new - for new files being uploaded to gcp
main - for storing processed files

Create the following secrets:

facebook_ad_account_zoom
facebook_ad_account_supplier_activity
facebook_access_token
facebook_app_id
facebook_app_secret

ad accounts are different, but access token, app id and secret will stay the same as it uses same app.

access token needs to be updated every 60 days

Create cloud functions:

trigger type: HTTP
require authentication
memory allocated: 1gb is probably fine
timeout: 540 - maximum run time
runtime service account: use service account with secret manager access

For facebook api:

create runtime environment variables:
project_id
upload_bucket

edit entry point to be either function in the main.py file

for facebook gcs to gbq:

create runtime environment variables:
project_id
upload_bucket - the new file storage bucket
new_bucket - the main storage bucket
bigquery_import_table - the table in which our daily data will be uploaded to
bigquery_main_table - the table in which our daily data will be inserted into - - contains all data

bigquery import and main tables require dataset too e.g. dataset.table

this function will create the import table but i believe you will need to manually create the main table

Create workflow:

    use service account with access to cloud functions
    enter workflow yaml file.

Create cloud schedule:

    frequency: use cron format - probably wouldn't run both these functions at same time just in case api limits
    target type: HTTP
    url: url link to workflow (see https://cloud.google.com/workflows/docs/schedule-workflow for url format)
    HTTP method: POST
    Auth Header: Add OAuth Token
    Service account: service account with access to workflows
