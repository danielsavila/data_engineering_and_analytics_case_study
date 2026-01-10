import os
import pyodbc
import struct
from azure.identity import DefaultAzureCredential
import pandas as pd
import urllib
from sqlalchemy import create_engine

server = "tcp:daniel-sql-server.database.windows.net"
database = "etl_pipeline_projects"
credential = DefaultAzureCredential()

token = credential.get_token("https://database.windows.net/.default")
access_token = token.token.encode("utf-16-le")

conn_str = (f"Driver={{ODBC Driver 18 for SQL Server}};"
            f"Server={server};"
            f"Database={database};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Authentication=ActiveDirectoryAccessToken;")

params = urllib.parse.quote_plus(conn_str)

def load(df):
    # use connection string to connect to database  
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", connect_args ={"attrs_before": {1256: access_token}})

    # load data to sql database
    df.to_sql("loaded_data", con = engine, if_exists = "replace", index = False)

    return print ("data loaded to azure sql database")