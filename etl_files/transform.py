import pandas as pd
import numpy as np

from dotenv import load_dotenv
load_dotenv()

def transform(df: pd.DataFrame):
    #check for missing values in the first 5 float columns
    if df.loc[:, "tasks":"costs"].isnull().values.any():
        df.fillna(0, inplace = True)

    #creating new columns
    df["profit"] = df["revenue"] - df["costs"]
    df["ovrtme_hours_ratio"] = df["overtime_hours"] / df["hours_worked"]
    
    #sorting values by date
    df = df.sort_values(by = "date")
    print("data transformed successfully")
    return df
