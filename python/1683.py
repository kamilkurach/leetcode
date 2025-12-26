import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.where(tweets['content'].str.len() > 15).filter(items=['tweet_id']).dropna()
