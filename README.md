## 🚀 What It Does
A small, functional sentiment analysis API built with FastAPI. It classifies input text as **positive**, **negative**, or **neutral** using TextBlob.

## 🛠️ How to Run

### Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### With Docker
```bash
docker build -t sentiment-analyzer .
docker run -p 8000:8000 sentiment-analyzer
```
### Example
```bash
curl -X POST "http://localhost:8000/analyze" \
-H "Content-Type: application/json" \
-d '{"text": "I love this!"}'
```

### Test
```bash
pytest
```


