import os, random
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


# Import the needed management objects from the libraries. The azure.common library
# is installed automatically with the other libraries.
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import ContainerClient
# Acquire a credential object using CLI-based authentication.



# Import the client object from the SDK library
from azure.storage.blob import BlobClient
credential = AzureCliCredential()
# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account.
connect_str = "DefaultEndpointsProtocol=https;AccountName=b680020bcsachin;AccountKey=5HvFQKKZ0xmYBwLO4boFHaSWGcIdmmH1enVRyX1l15REDNk37CrgDee42puwDNil3RqC2Kq0vzaTGtun06Anmg==;EndpointSuffix=core.windows.net"
container_client = ContainerClient.from_connection_string(connect_str, container_name="bcsachin-container-01")
blobs_list = container_client.list_blobs()
for blob in blobs_list:
    print(blob.name + '\n')