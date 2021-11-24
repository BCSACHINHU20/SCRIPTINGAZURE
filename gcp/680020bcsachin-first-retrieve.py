from google.cloud import storage


def list_blobs():
    """Lists all the blobs in the bucket."""
    bucket_name = "680020bcsachin-bucket"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)
list_blobs()