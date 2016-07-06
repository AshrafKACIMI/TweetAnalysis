consumer_key =  "rmiMS8UynVwTHbM1KSlfyEMF6"
consumer_secret =  "0Y58pO4DvlwS7xDXPS0IfFnuhh1EBZVYfmOll6o6TAvrePwY1V" 

access_token = "2614503361-pdmpYpcl79p1oHw5qG6yiK9aspHmpEbbhxqr4qP"
access_token_secret = "MurYNJJ3KVsLhfmRI82NeA1l61UzYDoYEiDLhlxScQly3"

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
c = 0
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print tweet.text
    r = collection.insert(tweet)
    print r
    c += 1

print "end insert"
tweets_iterator = collection.find()
for tweet in tweets_iterator:
  print tweet['text']








