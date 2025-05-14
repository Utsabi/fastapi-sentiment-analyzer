## What It Does
A small, functional sentiment analysis API built with FastAPI. It classifies input text as **positive**, **negative**, or **neutral** using TextBlob.

##  How to Run

### Locally
```bash
pip install -r requirement.txt
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

# Demo Video:
https://www.loom.com/share/2b94ca48dbe248b0b8b8cc954aca7a59?sid=7def08cb-3835-403c-a203-d7529114c141
# Github Repo:
https://github.com/Utsabi/fastapi-sentiment-analyzer


