consumer_key =  ""
consumer_secret =  "" 

access_token = ""
access_token_secret = ""

import os
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener

from pymongo import MongoClient
import json

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

client = MongoClient('localhost', 27017)
db = client['twitter_db']
collection = db['twitter_collection']

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print tweet.text
    r = collection.insert(tweet)
    print r

print "end insert"
tweets_iterator = collection.find()
for tweet in tweets_iterator:
  print tweet['text']








