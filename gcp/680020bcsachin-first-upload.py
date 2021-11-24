from google.cloud import storage


def upload_blob():
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    bucket_name = "680020bcsachin-bucket"
    # The path to your file to upload
    source_file_name = "bcs1.png"
    # The ID of your GCS object
    destination_blob_name = "680020bcsachinbcs1"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
upload_blob()

