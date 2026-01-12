<!-- ABOUT THIS PROJECT -->
# About this Data Engineering Case Study

This repo contains a real case study of data engineering and analytics consulting work done for a client for Atlas Consulting LLC.

The contents of this repo are organized in the following manner ...
1. Historical Context and Problem
2. Approach
3. Files
4. Outcomes

## Historical Context and Problem
The client approached Atlas Consulting with the following problem:
They had an ERP that provided project-driven resource management, budgeting, 
accounting, and expense reporting services. The ERP housed data in a data lake and provided an 
API to access that data. The client did not have the technical expertise 
to use this data for internal process improvement. Therefore, the data existed but 
provided little to no organizational value outside of historical record keeping.

The ERP had a front-end that allowed its users to manually query data and build reports.
Internal teams that wanted to do quarterly reporting, or department heads that wanted to do
monthly internal resource management, were required to use the front-end application to query data, 
manually copy individual rows from the front end reporting tool (no csv download available) 
into custom excel spreadsheets, and produce visualizations manually each quarter. 
On top of the manual labor required for this process, the front-end was not particularly
intuitive and staff reported significant frustration in working with the ERP provider.

## Approach
I wanted to utilize as many existing resources as possible in this solution, which meant leveraging
the Azure SQL Server that the client already maintained. The goals of this implementation were to... 

1. reduce employee hours and frustration spent interacting with the ERP front-end
2. automate workflows to reduce employee hours on repeateable tasks
3. reduce the potential for errors from manual data entry
4. enable the client to realize the full potential of their data for internal process improvement

To accomplish the above goals, I implemented the following...
1. Produced an ETL pipeline that extracted data from the ERP data lake.
2. The pipeline was containerized with the image saved to the client's Azure Container Registry
3. The container was scheduled to run weekly and store data in the client's Azure SQL database
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
5. Dockerfile
   - This dockerfile installs various system dependencies for retreiving Azure Entra ID token authentication, as well as
     ODBC drivers for connecting to the SQL database.

## Outcomes
Implementing this approach saved the client 50+ accounting hours per quarter on producing internal reports.
We eliminated manual data entry errors, standardized their reporting, and alleviated the frustrations that
staff reported in interacting with the ERP front-end. We also improved the organizations data-informed decision
making by visualizing their data in PowerBI. Department heads were able to better manage employee time,
prioritize projects that were underutilized, and improve allocation of resources for employee professional
development. 
