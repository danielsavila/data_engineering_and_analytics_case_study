import os, uuid
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

credential = ClientSecretCredential(
    tenant_id = 
)

try:
    print("connecting to blob storage")
    account_url = "https://azureblob101.blob.core.windows.net"
    default_credential = DefaultAzureCredential() 

    #identifying the client    
    blob_service_client = BlobServiceClient(account_url, credential=default_credential)

    #identifying the container
    container_name = "etl-project-raw-data"
    container_client = blob_service_client.get_container_client(container_name)

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

except Exception as ex:
    print('Exception:')
    print(ex)
