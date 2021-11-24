import os
from azure.identity import AzureCliCredential

# Import the client object from the SDK library
from azure.storage.blob import BlobClient

credential = AzureCliCredential()

# Retrieve the storage blob service URL, which is of the form
# https://pythonsdkstorage12345.blob.core.windows.net/
storage_url = "https://b680020bcsachin.blob.core.windows.net/bcsachin-container-01?sp=racwdli&st=2021-11-24T18:57:21Z&se=2021-11-25T02:57:21Z&sv=2020-08-04&sr=c&sig=H09tP9N07yhGFHz9R5P5Ue70rVbIzUJkyB1lArTwjTU%3D"
 

# Create the client object using the storage URL and the credential
blob_client = BlobClient(storage_url,
    container_name="bcsachin-container-01", blob_name="sachin-blob1.txt", credential=credential)

# Open a local file and upload its contents to Blob Storage
with open("sachin1.txt", "rb") as data:
    blob_client.upload_blob(data)