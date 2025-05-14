from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment import analyze_sentiment

app = FastAPI()

class TextRequest(BaseModel):
    text:str

@app.post("/analyze")
def analyze(request: TextRequest):
    result = analyze_sentiment(request.text)
    return {"Sentiment": result}