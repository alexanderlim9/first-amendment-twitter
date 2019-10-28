import os
import tweepy as tw
import pandas as pd
import config

auth = tw.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#firstamendment"
date_since = "2019-10-14"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(50)
              
# Store tweets in array and then pandas dataframe
arr = []

for tweet in tweets:
    follow_trump = api.show_friendship(tweet.user.id_str, tweet.user.screen_name, '25073877', 'realDonaldTrump')[0].following
    follow_clinton = api.show_friendship(tweet.user.id_str, tweet.user.screen_name, '1339835893', 'HillaryClinton')[0].following
    
    arr.append({'created at': tweet.created_at, 'text': tweet.text, 'retweets': tweet.retweet_count, 'likes': tweet.favorite_count, 'follows trump': follow_trump, 'follows clinton': follow_clinton})

pd.DataFrame(arr)