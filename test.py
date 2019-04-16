import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import io 
import json 

config_file = '_cleTweet.json'
with open( config_file) as cf : 
	config = json.load(cf)

ckey = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token_key = config['access_token']
access_token_secret = config['access_token_secret']


start_time = time.time() #grabs the system time

class listener(StreamListener):
 
	def __init__(self, start_time, time_limit=60):
 
		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []
 
	def on_data(self, data):
 
		saveFile = io.open('donnee.json', 'a', encoding='utf-8')
 
		while (time.time() - self.time) < self.limit:
 
			try:
				self.tweet_data.append(data)
				return True
 
 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
 
		saveFile = io.open('donnee.json', 'w', encoding='utf-8')
		saveFile.write(u'[\n')
		saveFile.write(','.join(self.tweet_data))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()
 
	def on_error(self, status):
 
		print status

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)
 
 
twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=['psg'], languages=['fr']) 

