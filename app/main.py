from fastapi import FastAPI
from pattern.en import sentiment

# from app.nlp import clean_text, correct_text, predict_sentiment

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
    return {"message": "Hello World it is the Big Data & Joropo team API"}

@app.post("/sentimet/{review}")
async def sentiment_analisys_on_reviews(review:str):
    return sentiment(review)
