import os
import tweepy as tw
import pandas as pd
import numpy
import csv
import config

auth = tw.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#firstamendment"
date_since = "2019-10-10"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(1000)
              
# Store tweets in array and then pandas dataframe
# arr = []

# for tweet in tweets:
#     follow_trump = api.show_friendship(tweet.user.id_str, tweet.user.screen_name, '25073877', 'realDonaldTrump')[0].following
#     follow_clinton = api.show_friendship(tweet.user.id_str, tweet.user.screen_name, '1339835893', 'HillaryClinton')[0].following
    
#     arr.append({'created at': tweet.created_at, 'text': tweet.text, 'retweets': tweet.retweet_count, 'likes': tweet.favorite_count, 'follows trump': follow_trump, 'follows clinton': follow_clinton})

# pd.DataFrame(arr)

with open('tweets-11-11.csv', 'w', newline='') as f:
    count = 0
    writer = csv.writer(f)
    writer.writerow(['created at', 'text', 'retweets', 'likes', 'follows trump', 'follows clinton'])
    for tweet in tweets:
        count = count+1
        print(count)
        follow_trump = api.show_friendship(tweet.user.id_str, tweet.user.screen_name, '25073877', 'realDonaldTrump')[0].following
        follow_clinton = api.show_friendship(tweet.user.id_str, tweet.user.screen_name, '1339835893', 'HillaryClinton')[0].following

        writer.writerow([tweet.created_at, tweet.text.replace(',', '').encode('utf-8'), tweet.retweet_count, tweet.favorite_count, follow_trump, follow_clinton])
    
# plt.show()