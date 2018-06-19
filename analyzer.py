'''
This program will analyze the sentiment level of the person who tweets about 
a specific topic and will give out a user friendly score to the user about
the tweets sentiment level. 

This Program intends to showcase a glimpse of common natural language processing (NLP)

'''
import tweepy
from textblob import TextBlob
import config

# Twitter consumer keys and access tokens
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret

access_token = config.access_token
access_token_secret = config.access_token_secret

# Authenticating the app with twitter via tweepy's OAuthHandler()
# This method takes in consumer_key and consumer_secret as params respectively
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

# Will set the access token and access token secret to our OAuthHandler var
auth.set_access_token(access_token,access_token_secret)

# Will create a var off tweepy API object
# this can be used for all twitter methods that we need for our app
api = tweepy.API(auth)

# Search for all the tweets with the specified keyword
public_tweets = api.search('Buddhi')

for tweet in public_tweets:
    print(tweet.text)
    # Performing sentiment analysis
    analysis = TextBlob(tweet.text)
    # Printing the analysis result
    print(analysis.sentiment)
    if analysis.sentiment.polarity<0:
        print('Its a negative feeling ')
        if analysis.sentiment.subjectivity<0.5:
            print('Its objective ')
        elif analysis.sentiment.subjectivity>0.5:
            print('Its subjective ')
    elif analysis.sentiment.polarity>0:
        print('Its a positive feeling ')
        if analysis.sentiment.subjectivity<0.5:
            print('Its objective ')
        elif analysis.sentiment.subjectivity>0.5:
            print('Its subjective ')



