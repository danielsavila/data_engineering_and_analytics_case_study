import pandas as pd
import numpy as np

#creating random numeric values
df = pd.DataFrame()

df["tasks"] = np.random.choice(np.arange(50, 150), size = 200, replace = True)
df["hours_worked"] = np.random.choice(np.arange(20, 200), size = 200, replace = True)
df["overtime_hours"] = np.random.choice(np.arange(0, 50), size = 200, replace = True)
df["revenue"] = np.random.choice(np.arange(1000, 10000), size = 200, replace = True)
df["costs"] = np.random.choice(np.arange(500, 8000), size = 200, replace = True)

#creating department categories
df["dept_key"] = np.random.choice(np.arange(6), size = 200, replace = True)

departments = ["FINANCE", "ENVIRONMENT", "ECON_DEVELOPMENT", "EDUCATION", "AGRICULTURE", "CORPORATE_SERVICES"]
dept_abv = ["FINA", "ENVI", "ECON", "EDUC", "AGRI", "CORP"]

dept_key = np.random.choice([0, 1, 2, 3, 4, 5], size = 6, replace = False)
department = pd.DataFrame({"department": departments,
                           "dept_abv": dept_abv,
                           "dept_key" : dept_key})

df = pd.merge(df, department, on = "dept_key", how = "left").drop(columns = "dept_key")


#creating transaction dates
dates = np.random.choice(pd.date_range(start = "10/15/2024", end = "1/7/2026"), size = 200, replace = True)
dates = pd.to_datetime(dates)
df["date"] = dates
df = df.sort_values(by = "date").reset_index(drop = True)

df.to_csv("data.csv", index = False)