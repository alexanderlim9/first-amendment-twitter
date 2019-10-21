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
              since=date_since).items(15)
              
# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)