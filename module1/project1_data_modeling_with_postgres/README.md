# Data Modeling with Postgres

## Project Description

Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

In Sparkify it's essential to keep aligned with the users' tastes to be able to provide a personalized experience. The aim of the project is to leverage data by utilizing the already existing data sets to drive possibilities for new services, applications, and capabilities. And that through building a Postgres DB to hold the data using a schema and ETL pipeline that is designed with alignment to the business needs to make finding answers easier and more efficient by optimizing queries on song play analysis 


## Technical Requirements

To run the ETL scripts, the system needs to fullfill the following requirements:
    1. Python 3.x 
    2. `pandas` and `psycopg2` external libraries should be available
    3. The scripts could be rum through the terminal using the following command:
    `python.exe script_file_path`

## Project Anatomy


The ETL consists of three main files, as follows:
* sql_queries.py: holds the abstract for creating the DB. Tables creation, data insertion, and retrival queries to be used later on the next setp in the pipeline.
* create_tables.py: This is the second station of the pipeline which consumes the queries from the sql_queries script and run it against the PostgreAQL server to create the Physical DB
* etl.py: The final and core station that leverages the DB to transform data and drvie findings to answer the business questions. 

## The Design Motivation

The DB is designed using the Star Schema; whic is more optimized for analytical purposes on historical data (OLAP)  as it is primarily read optimized that expected to deliver good performance over large data sets.

While building the pipline we considered separating logical from the physical database design and creation and those are the first two stations of the pipeline. The third and last station of the pipeline is the data ingestion, insertion, and transformation all together. 

The follolwing is an illustration of the DB which is consists of one Fact table `songplays` and four dimension tables `time`, `users`, `artists`, and `songs`.


![](https://i.imgur.com/L0Ew60S.png)
