import tweepy
import pandas as pd

bearer_token = "AAAAAAAAAAAAAAAAAAAAAEPe0QEAAAAAsU%2ByZBpTRIeBBkHYyP2eQ1FSrCQ%3DD3AJSZ6hP6io3CaWb6H9dgcPEnX535sHdQPAQTThSOdG8LfjQh"

def get_tweets(topic):
    client = tweepy.Client(bearer_token=bearer_token)

    query = f"{topic} lang:en -is:retweet"
    tweets = tweepy.Paginator(
        client.search_recent_tweets, 
        query=query, 
        tweet_fields=['created_at', 'lang', 'text'], 
        max_results=30  # this controls per page
    ).flatten(limit=30)  # this controls total tweets fetched

    tweet_data = []

    for tweet in tweets:
        tweet_data.append({
            'date': tweet.created_at,
            'text': tweet.text
        })

    return pd.DataFrame(tweet_data)
