import pandas as pd
from src.scraper import get_tweets
from src.sentiment import clean_text, get_sentiment
from src.visualize import plot_sentiment_bar, show_wordcloud

topics = [
    "Artificial Intelligence",
    "Electric Vehicles",
    "Stock Market",
    "Crypto News"
]

for topic in topics:
    # Get tweets for the topic
    df = get_tweets(topic)

    # Clean and analyze sentiment
    df["Cleaned_Tweet"] = df["text"].apply(clean_text)
    df["Sentiment"] = df["Cleaned_Tweet"].apply(get_sentiment)

    # Print sample output
    print(f"\n==== {topic.upper()} ====")
    print(df.head())

    # Save to CSV
    df.to_csv(f"{topic.replace(' ', '_').lower()}_output.csv", index=False)

    # Visualizations per topic
    plot_sentiment_bar(df)
    show_wordcloud(df)
