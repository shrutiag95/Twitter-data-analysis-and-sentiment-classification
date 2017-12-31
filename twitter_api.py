from tweepy import Stream
from tweepy import OAuthHandler
import tweepy
from tweepy.streaming import StreamListener
import twitter_sentimental_analysis module as s
import json


#consumer key, consumer secret, access token, access secret.
ckey="KQdYshiJoovMH2kI2JTX5kP4j"
csecret="IHIkFiyw3VqvcoPXvKJ1h47K7RHBOKow57YsFSUpkfdJthIY55"
atoken="864365274023067648-9ZTclQ8tKrk9Wkjs4TkzLj4QKlvEBDR"
asecret="KKZWlYdlhhizVJn9kfPDVKdz4QPWzdw6xIBC46CBFFfN6"

class listener(StreamListener):

    def on_data(self, data):
       try:
            
           all_data = json.loads(data)
           tweet = all_data["text"]
           classification_result,confidence=s.sentiment(tweet)
          
       except:
           print(True)
            
           
       return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Any word or hashtag"])
