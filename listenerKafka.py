from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
from kafka.client import SimpleClient
from kafka.consumer import SimpleConsumer
import os,io,json

#listenerKafka

producer = KafkaProducer(bootstrap_servers='master:6667',value_serializer=lambda x: json.dumps(x).encode('utf-8'))
config_file = '_cleTweet.json'
with open( config_file) as cf :
    config = json.load(cf)

consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_token_secret = config['access_token_secret']

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send('foot', str(data))
        print(data)
        return True
        def on_error(self, status):
            print(status)
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['psg'],languages=["fr"])
