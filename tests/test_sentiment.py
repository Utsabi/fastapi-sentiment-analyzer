from app.sentiment import analyze_sentiment


def test_positive_sentiment():
    assert analyze_sentiment("I love it!") == "positive"


def test_negative_setiment():
    assert analyze_sentiment("I hate it!") == "negative"
