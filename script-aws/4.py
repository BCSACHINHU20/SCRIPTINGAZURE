import logging
import boto3
import os
import glob

from botocore.exceptions import ClientError


def create_bucket(bucket_name, region):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
create_bucket("b680020bcsachin-bucket", region="us-east-2")

BUCKET_NAME = 'b680020bcsachin-bucket'
FOLDER_NAME = './'

session = boto3.Session(profile_name='default')
s3 = session.client('s3')

csv_files = glob.glob("*.csv")
json_files = glob.glob("*.json")

for filename in csv_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.upload_file(filename, BUCKET_NAME, key)

for filename in json_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.upload_file(filename, BUCKET_NAME, key)

print("All_Done")