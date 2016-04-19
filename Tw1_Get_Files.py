# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:19:26 2016

@author: ArmandoLC
"""

#Tw1_GetFiles
'''
Con este script importo todos los archivos de una carpeta. Los archivos representan
los tweets obtenidos con streaming. Cada archivo representa una hora de streaming
Tweets en formato json
'''
import os
from os import listdir
from os.path import isfile, join
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud#, STOPWORDS
import nltk
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("spanish")
#from nltk.corpus import stopwords # Import the stop word list
#print stopwords.words("english") 
#mypath=os.getcwd()
mypath='C:/Armando/2016/03/Nueva carpeta'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
sample=onlyfiles[10]
tweets_data = []
num_collections=len(onlyfiles)
for element in range(0,num_collections-1):
    filename=onlyfiles[element]
    tweets_data_path = 'C:/Armando/2016/03/Nueva carpeta/'+filename
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            if tweet['lang']=='es':
                tweets_data.append(tweet)
        except:
            continue

tweet.keys()  #para saber los campos del json


