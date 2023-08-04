# factored-datathon-2023-Big-Data-Joropo
This repository contains the source code developed and all of the related files by the Big Data & Joropo team for the Datathon Factored 2023. <br />
Index:
- Project Summary
- Data Extraction
- Data Transformation
- Machine Learning
- Data Analytics

## Project Summary
[redactar resumen]

## Data Extraction
Contains Python scripts used in the Data Engineering phase to download the data partitions hosted in Azure.

## Data Transformation
Contains Python and Jupyter Notebooks used to clean and prepare the two datasets: metadata and reviews.

### Metadata
data_cleaning_metadata.ipynb: cleaning each of the 15 partitions of metadata and transforming to parquet files.
- Removed the columns "details.X", "tech1", "tech2", "fit" and "similar_item".
- Transformation of the columns "image", "category" and "rank" into useful versions: "image_count", "category_count" and "rank_in_category".
- Replacing useless values with nulls, changing data types and data formats like the "price" column.
- Creation of the columns "also_buy_count" and "also_view_count".

eda_all_metadata.ipynb: receives all of the preprocessed partitions. The outputs are the cleaned metadata of books and the lists of book asin's used in the reviews data preparation.
- Concat all of the pre-processed partitions and filter by books only.
- Drop the columns: "also_buy","also_view","date","main_category"
- Drop rows with invalid "brand" names
- Drop rows with nulls

## Machine Learning
-

## Data Analytics
Link the Power BI Dashboard

Python scripts used in the data engineering phase to download the data partitions hosted in azure

Power BI Dashboard where valuable insights are shown from the provided review and metadata files, the dashboard can be seen here []

API developed to obtain the sentiment analysis of a review, this API was developed with python and deployed in a docker container in the Render provider, you can visit the API and its documentation [here](https://joropo-factored.onrender.com/docs)

Jupyter notebook and model of a product recommendation system.

Tools and libraries used:
        Visual Studio Code
        Jupyter Notebook

        Power BI

        Python

        Pattern     (library)
        MLFlow      (library)
        Tensorflow  (library)

