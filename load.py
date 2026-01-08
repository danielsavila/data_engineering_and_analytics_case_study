import os
from dotenv import load_dotenv
import urllib
from sqlalchemy import create_engine
load_dotenv()


def load(df):
    # authenticating azure sql server connection
    server = os.environ["SQL_SERVER"]
    database = os.environ["SQL_DATABASE"]

    # writing data to azure sql server
    # connecting to sql server with connection string
    conn_str = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={server},1433;"
    f"Database={database};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Authentication=ActiveDirectoryMsi;"
    )

    params = urllib.parse.quote_plus(conn_str)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


    df.to_sql("loaded_data", con = engine, if_exists = "replace", index = False)

    return print ("data loaded to azure sql database")

