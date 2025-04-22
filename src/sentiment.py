import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^A-Za-z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    if score["compound"] > 0.05:
        return "Positive"
    elif score["compound"] < -0.05:
        return "Negative"
    else:
        return "Neutral"
