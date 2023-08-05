from fastapi import FastAPI
from pattern.en import sentiment
from app.predict import get_prediction
import tensorflow as tf
import json

description = """
You will be able to:
* Predict the sentiment on a given review
* Get product recommdation for user

Sentiment analysis:
This method makes use of the Pattern library to generate the sentiment of a reviews, 
at the same time it generates a confidence measurement that supports said sentiment.

Book recommendation:
This model is trained based on 330K products belonging to the Books category of the total existing categories
A neural network was developed using the TensorFlow Recommender System library

Instructions for using the API

Click on the method you want to use:
* /sentiment/{review}
* /recommend/{reviewerid}

Click the "Try it out" button

Type the Review or Reviewer ID in the corresponding field.

Click on the "Execute" button.

Scroll to the bottom to the "Response" section specifically to the "Response body" section

In the case of sentiment analysis, you will obtain two decimal numbers which correspond to sentiment analysis and confidense.
The first number corresponded to the sentiment of the review, if it is positive the sentiment will be classified as Affirmative, 
if it is a negative number the sentiment will be classified as Negative.
The second number returned corresponds to the level of confidence with which the method supports the predicted sentiment.

In the case of the method for recommendations, it will return a list with 10 titles of the recommended free books.

"""

app = FastAPI(
    title="BigDataJoropoAPI",
    description=description,
    summary="API of Big Data & Joropo Team 🚀",
    version="0.0.1",
)
path_model = 'app/models'

@app.get("/")
async def root():
    return {"message": "Hello World it is the Big Data & Joropo team API"}

@app.post("/sentimet/{review}")
async def sentiment_analisys_on_reviews(review:str):
    return sentiment(review)

@app.post("/recommend/{reviewerid}")
async def recommend_products(reviewerid:str):
    return get_prediction(reviewerid)
