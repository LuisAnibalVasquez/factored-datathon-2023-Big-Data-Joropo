from fastapi import FastAPI
from pattern.en import sentiment
from app.predict import get_prediction
import tensorflow as tf
import json

description = """
You will be able to:
* Predict the sentiment on a given review
* Get product recommdation for user
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
