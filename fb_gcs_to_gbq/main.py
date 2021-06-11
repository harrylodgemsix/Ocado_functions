import os
from re import L

import fsspec
import gcsfs
import pandas as pd
from google.cloud import bigquery, storage
from numpy.lib.utils import source

from mover_functions import fb_query, fb_transform, move_blob

# the project id
project_id = os.environ["project_id"]

# the bucket where your daily csv files get uploaded to
bucket = os.environ["upload_bucket"]

# the bucket where you will be storing your csv after processing
new_bucket = os.environ["new_bucket"]

# the bigquery table where you will upload your daily csv data
bigquery_import_table = os.environ["bigquery_import_table"]

# the bigquery table which will contain all data
bigquery_main_table = os.environ["bigquery_main_table"]


def fb_gcs_to_gbq_zoom(request):

    fb_transform(bucket, "fb/", bigquery_import_table, project_id)
    fb_query(bigquery_import_table, bigquery_main_table)
    move_blob(bucket, new_bucket, "fb/zoom/")

    return {"status": "success"}


def fb_gcs_to_gbq_supplier_activity(request):

    fb_transform(bucket, "fb/", bigquery_import_table, project_id)
    fb_query(bigquery_import_table, bigquery_main_table)
    move_blob(bucket, new_bucket, "fb/supplier_activity/")

    return {"status": "success"}
