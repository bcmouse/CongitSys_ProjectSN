# coding=utf-8
import facebook
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd
import unicodedata
import matplotlib.pyplot as plt
from wordcloud import WordCloud


tok = 'CAACEdEose0cBAAMGlt2g7s8mA9ln6cZCSN42m2S95u2UDn6J60fZBrdyc3hXiEZBW6ukeI3KAZAd7zdaiELWHL773FibWlhNf0jUweovEuAy3kDoSbCHwpC422TtmyzXOncGsfyZAeU1uQQLJrg31sfZBgZCPSy99hcgZCVjtJxZAPHmBPsu0xglGqqZCRZB2wJOVf4y6fo5Kd5KahIHxMrHnr9'# Add a valid facebook token

# Create a connection to the Graph API with your access token
g = facebook.GraphAPI(access_token=tok, version='2.2')
# Execute a few sample queries
user_id = '694361250580489' #add the facebook id to mine

Plim = str(20) #Limit of post to be analyzed

posts = g.get_object(user_id, fields = 'posts.limit('+Plim+').fields(created_time,message,comments.fields(created_time,from,message))')

client = MongoClient("localhost", 27017)
db = client.Fposts
collection = db.test

line = json.dumps(posts)

try:
    if line:
        try:

            lineJson = json.loads(line)
        except (ValueError, KeyError, TypeError) as e:
            pass
        else:
            PostId = collection.insert(lineJson)
            print 'inserted with id: ', PostId

except (ValueError, KeyError, TypeError) as e:
        print e

cursor = collection.find({"_id": ObjectId(''+str(PostId)+'')},{"posts.data.message": 1, "posts.data.comments.data.message": 1})

print(cursor.count())
words = ''
try:
    for document in cursor:
        posts = document['posts']
        data = posts['data']
        for message in data:
            #print(message['message'])
            words = words+' '+message['message']
            comments = message['comments']
            data2 = comments['data']
            for message2 in data2:
                #print(message2['message'])
                words = words+' '+message2['message']

except (ValueError, KeyError, TypeError) as e:
        print e
words = words.replace('\n', ' ')
#print(words)

STOPWORDS = set([x.strip() for x in open('C:\\Users\\Luis\\Downloads\\stopwords_es.txt').read().split('\n')])

wordcloud = WordCloud(
                      stopwords=STOPWORDS,
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(words)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./my_twitter_wordcloud_1.png', dpi=300)
plt.show()
