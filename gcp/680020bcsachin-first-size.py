from google.cloud import storage


def list_blobs():
    """Lists all the blobs in the bucket."""
    bucket_name = "680020bcsachin-bucket"
    storage_client = storage.Client()
    totalsize =0
    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
       totalsize =totalsize+blob.size
    return totalsize

list_blobs()
print("total size =")
print(list_blobs())