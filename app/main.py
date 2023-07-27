from fastapi import FastAPI
from app.nlp import clean_text, correct_text, predict_sentiment

description = """
You will be able to:
* Predict the sentiment on a given review
"""

app = FastAPI(
    title="BigDataJoropoAPI",
    description=description,
    summary="API of Big Data & Joropo Team 🚀",
    version="0.0.1",
)
 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# This method allows you to predict the sentiment from the review
@app.post("/sentimet/{review}")
async def sentiment_analisys_on_reviews(review:str):
    clean_review = clean_text(review)
    correct_review = correct_text(clean_review)
    return predict_sentiment(correct_review)

