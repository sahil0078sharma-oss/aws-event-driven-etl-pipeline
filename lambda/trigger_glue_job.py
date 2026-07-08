"""
File: trigger_glue_job.py

Description:
This AWS Lambda function is automatically triggered whenever
a CSV file is uploaded to the 'older-data/' folder of the
Amazon S3 bucket. It starts an AWS Glue ETL job using boto3,
which processes the uploaded CSV and stores the cleaned output
in the target S3 folder.

Author: Sahil Sharma
Project: AWS Event-Driven ETL Pipeline
"""

import json
import boto3

# Create a Glue client
glue = boto3.client("glue")

def lambda_handler(event, context):
    """
    Triggered automatically when a CSV file is uploaded
    to the 'older-data/' folder in the S3 bucket.
    """

    # Extract bucket name and object key from the S3 event
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_key = event["Records"][0]["s3"]["object"]["key"]

    print("========== FILE DETAILS ==========")
    print(f"Bucket : {bucket_name}")
    print(f"File   : {file_key}")

    # Start the AWS Glue ETL job
    response = glue.start_job_run(
        JobName="aws-arya-etl-glue"
    )

    print("========== GLUE JOB STARTED ==========")
    print(response)

    return {
        "statusCode": 200,
        "body": json.dumps("Glue Job Started Successfully")
    }