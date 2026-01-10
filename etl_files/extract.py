import os
import pandas as pd
import io
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from sqlalchemy import create_engine
import urllib
load_dotenv()

# authenticating azure blob storage connection
credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
    )

account_url = "https://azureblob101.blob.core.windows.net"

def extract():
    # extract from azure blob storage
    print("connecting to blob storage")

    #identifying the client    
    blob_service_client = BlobServiceClient(account_url, credential = credential)

    #identifying the container and blob
    container_name = "etl-project-raw-data"
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client("data.csv")

    #stream this if file size is too large
    blob_data = blob_client.download_blob().readall()

    df = pd.read_csv(io.BytesIO(blob_data))
    print("data extracted successfully")
    return df
