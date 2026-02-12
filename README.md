<!-- ABOUT THIS PROJECT -->
# About this Data Engineering Case Study

This repo contains a case study of data engineering consulting work for Atlas Consulting LLC.

The contents of this repository are organized in the following manner...
1. Historical Context and Problem
2. Approach
3. Files
4. Outcomes

## Historical Context and Problem
Clients commonly approach Atlas Consulting LLC with the following problem:
Clients maintain data within an ERP containing budgeting, 
accounting, and expense reporting services. The client did not have the technical expertise 
to extract this data for evaluation/internal process improvement. Therefore, executive teams
stuggle to use this data for internal process improvement, the data sits
underutlized, and little to no organizational value can be derived of this data outside of 
internal record keeping.

Internal teams that wanted to do quarterly reporting, or department heads that wanted to do
monthly internal resource management were required to manually query data, 
copy output from the front end reporting tool (no csv download available) 
into custom excel spreadsheets, and produce custome visualizations each quarter. 
On top of the extensive manual labor required for basic internal reporting, the interface was 
difficult to interact with and staff reported significant frustration in using the tool.

## Approach
I wanted to leverage Microsoft Azure as much as possible, since many nonprofit data teams
already use Microsoft 365, or other Microsoft services/tools. The goals of this implementation were to... 

1. reduce reporting hours and employee frustration interacting with the ERP
2. automate workflows to reduce employee hours on repeateable tasks
3. reduce the potential for human error from manual data entry and copy/paste
4. enable near real-time data visualization for department leadership of internal metrics

To accomplish the above goals, I implemented the following...
1. Produced an ETL pipeline that extracted data from the ERP data lake.
2. The pipeline was containerized using Docker with the image saved to the client's Azure Container Registry
3. The container was scheduled to run nightly and store data in the client's Azure SQL database
4. Connect PowerBI to the database and visualize data via interactive dashboards

## Files
The documents included in this repo are the following...
1. creating_synthetic_data.py
   - Creating a synthetic data set to move and manipulate. This file was manually uploded to Azure Blob Storage.
2. extract.py
   - For this case study's purposes, we extract from Azure Blob Storage to simulate extracting from the client's data lake.
3. transform.py
   - Take in the extractred data and add two new columns
4. load.py
   - Take transformed data, connect to an Azure SQL database, and load for storage.
5. main.py
   - Since the size of the data pull is relatively small, we perfoemd the ETL process in one function. Further improvements would include more detailed logging of events and an Airflow DAG to implemment retries...etc.
5. Dockerfile
   - This dockerfile installs various system dependencies for retreiving Azure Entra ID token authentication, as well as
     ODBC drivers for connecting to the SQL database.

## Outcomes
Implementing this approach saved the client >50+ accounting hours per quarter on internal reporting.
We eliminated manual data entry errors, standardized their reporting across months, and eliminated frustrations 
from interacting with the ERP. We also improved the organizations data-informed decision-making by visualizing 
their data in PowerBI. Department heads were able to better manage employee time,
prioritize projects that were underutilized, and improve allocation of resources for employee professional
development. In leveraging Azure Container Resources and its Managed Identities functionality, we minimized
cybersecurity concerns by implementing the container image in the organization's Azure Container Registry, 
the container image's read/write authentication, and the PowerBI dashboard without increasing the number of 
username/password combinations or employee access requirements.
