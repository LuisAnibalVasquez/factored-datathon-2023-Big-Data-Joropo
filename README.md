# factored-datathon-2023-Big-Data-Joropo
This repository contains the source code developed and all of the related files by the Big Data & Joropo team for the Datathon Factored 2023. <br />

Index:
- Project Summary
- Data Extraction
- Data Transformation
- Machine Learning
- App
- Data Analytics

## Project Summary
The following project aims to provide an end-to-end dashboard for retailers and ecommerce business, using Amazon product review data
It can be used to track product performance, identify trends, and make informed decisions about pricing and marketing.
- Data collection: The data was collected from the Microsoft Azure Data Lake & Microsoft Azure Event Data Hub. It provides access to a variety of product review data, including the product name, price, rating, number of reviews, and star rating.
- Data cleaning: The data was cleaned to remove any errors or inconsistencies. This included removing duplicate records, fixing typos, and standardizing the data format.
- Data analysis: The data was analyzed to identify trends and patterns. This included calculating the average rating for each product category, the distribution of ratings, among others.
- Dashboard development: A Power BI dashboard was developed to visualize the data analysis results. The dashboard includes a variety of charts and graphs that make it easy to understand the data.

![alt text](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/references/data_pipeline.png?raw=true)


## Data Extraction
Contains Python scripts used in the Data Engineering phase to download the data partitions hosted in Azure.

### Batch
[01_fetch_batch.py](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/Data%20Extraction/01_fetch_batch.py): fetching the batch data

### Stream
[02_fetch_stream.py](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/Data%20Extraction/02_fetch_stream.py): fetching the streaming data

## Data Transformation
Contains Python and Jupyter Notebooks used to clean and prepare the two datasets: metadata and reviews.

### Metadata
[03_data_cleaning_metadata.ipynb](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/Data%20Transformation/03_data_cleaning_metadata.ipynb): cleaning each of the 15 partitions of metadata and transforming to parquet files.
- Removed the columns "details.X", "tech1", "tech2", "fit" and "similar_item".
- Transformation of the columns "image", "category" and "rank" into useful versions: "image_count", "category_count" and "rank_in_category".
- Replacing useless values with nulls, changing data types and data formats like the "price" column.
- Creation of the columns "also_buy_count" and "also_view_count".

[04_data_cleaning_metadata_books.ipynb](04_data_cleaning_metadata_books.ipynb): receives all of the preprocessed partitions. The outputs are the cleaned metadata of books and the lists of book asin's used in the reviews data preparation.
- Concat all of the pre-processed partitions and filter by books only (2.8M books).
- Drop the columns: "also_buy","also_view","date","main_category"
- Drop rows with invalid "brand" names.
- Drop rows with nulls (383k books remaining).
- Filter only the books placed in the Top 25k Rank to be used with reviews for Machine Learning (list of 12k books).

### Reviews
[05_data_cleaning_reviews.py](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/Data%20Transformation/05_data_cleaning_reviews.py): filters all of the reviews extracted to only show the records associated with the books in the Top 25k rank by category.

## Machine Learning
- [06_sentiment_confidence_analisis.py](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/Machine%20Learning/06_sentiment_confidence_analisis.py):
This script makes the sentiment analysis
- [07_Join_Data_for_Recommender.ipynb](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/notebook/Join_Data_for_Recommender.ipynb):
This notebook allows you to concatenate and filter the data necessary to train the Machine Learning model.
- [08_Modeling_recommender_system.ipynb](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/Machine%20Learning/08_Modeling_recommender_system.ipynb)
Recommended system specs

- [Modeling_recommender_system.ipynb](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/notebook/Modeling_recommender_system.ipynb)
In this notebook the model for the Recommender System is created.

## API
- [main.py](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/app/main.py):
Entry point of the REST API, conformed by two POST method to determine the sentiment analysis of the review and book recommendation.

The API is deployed [here](https://joropo-factored.onrender.com/docs)

## APP
- [app.py](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/app.py)
It is a Streamlit application which consume the REST API and show sentiment and recommendation on demand.

The Streamlit App is deployed [here](https://joropo-factored-app.onrender.com/)

## Data Analytics
Power BI Dashboard where valuable insights are shown from the provided review and metadata files, the dashboard can be seen here
Link the Power BI Dashboard:

-[Here](https://app.powerbi.com/view?r=eyJrIjoiZjE4NDExYWYtM2M0NS00ZDI4LWE0ZDItZWY1ZmJlN2VlMmQ4IiwidCI6IjEyZDI2YWY0LTM2ZDUtNGUwMy1hMDJlLTJiNGMxMDc0ZTRlOCIsImMiOjJ9)

The key influencers visual may not be available for the online report view.  
You must be in the list of authorized emails.  
Contact the report owners for permission.  

Tools and libraries used:

        Visual Studio Code
        Jupyter Notebook

        Power BI

        Python

        MLFlow      
        Pattern     
        Stramlit
        Tensorflow  
        Tensorflow Recommenders
