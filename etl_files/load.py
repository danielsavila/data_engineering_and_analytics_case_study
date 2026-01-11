import struct
from azure.identity import DefaultAzureCredential
import urllib
from sqlalchemy import create_engine

server = "tcp:daniel-sql-server.database.windows.net"
database = "etl_pipeline_projects"
credential = DefaultAzureCredential()

conn_str = (f"Driver={{ODBC Driver 18 for SQL Server}};"
            f"Server={server};"
            f"Database={database};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Authentication=ActiveDirectoryMsi")

params = urllib.parse.quote_plus(conn_str)

def load(df):
    #accessing token from DefaultAzureCredential
    token = credential.get_token("https://database.windows.net/.default")
    access_token = bytes(token.token, "utf-8")
    token_struct = struct.pack(f"<I{len(access_token)}s", len(access_token), access_token)
    
    # use connection string to connect to database  
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}", connect_args ={"attrs_before": token_struct})

    # load data to sql database
    df.to_sql("loaded_data", con = engine, if_exists = "replace", index = False)

    return print ("data loaded to azure sql database")