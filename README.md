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
[redactar resumen]

## Data Extraction
Contains Python scripts used in the Data Engineering phase to download the data partitions hosted in Azure.

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

## Machine Learning
- [Join_Data_for_Recommender.ipynb](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/notebook/Join_Data_for_Recommender.ipynb):
This notebook allows you to concatenate and filter the data necessary to train the Machine Learning model.

- [Modeling_recommender_system.ipynb](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/notebook/Modeling_recommender_system.ipynb)
In this notebook the model for the Recommender System is created.

## APP
- [main.py](https://github.com/LuisAnibalVasquez/factored-datathon-2023-Big-Data-Joropo/blob/main/app/main.py):
Entry point of the REST API, conformed by a GET method to determine the sentiment analysis of the review.

The API is deployed [here](https://joropo-factored.onrender.com/docs)

## Data Analytics
Power BI Dashboard where valuable insights are shown from the provided review and metadata files, the dashboard can be seen here []
Link the Power BI Dashboard

Tools and libraries used:

        Visual Studio Code
        Jupyter Notebook

        Power BI

        Python

        Pattern     
        MLFlow      
        Tensorflow  
        Tensorflow Recommenders
