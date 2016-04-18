#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from pymongo import MongoClient


#Variables that contains the user credentials to access Twitter API
access_token = "159591091-NbmupY7NznYjz40zlsHacjanyeLremZEScy7PaTp"   #"ENTER YOUR ACCESS TOKEN"
access_token_secret = "43je0Kc4djzdA0tqauusl5sp57xjLYkWM3fbaRju1hj7V" #"ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "4WARWnJOGFVk49OmDUimkXbwa"  #"ENTER YOUR API KEY"
consumer_secret =  "PXKC8xsfVa41nb0OpJbuD4yLy5zx7ZFj4MDEJgRc5d8irHsPSi" #"ENTER YOUR API SECRET"

connection = MongoClient("mongodb://localhost")
db=connection.cooldb

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_connect(self):
        """Called when the connection is made"""
        print("You're connected to the streaming server.")

    def on_error(self, status_code):
        """This is called when an error occurs"""
        print('Error: ' + repr(status_code))
        return True

    def on_data(self, data):
        #client = MongoClient('localhost', 27017)

        # Use cooldb database
       # db = client.cooltweets

        # Decode JSON

        datajson = json.loads(data)

        # We only want to store tweets in Spanish
        if "lang" in datajson and datajson["lang"] == "es":
            # Store tweet info into the cooltweets collection.
            print data
            db.cooltweets.insert_one(datajson)
        return True




if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Moreira', 'Brozo'])