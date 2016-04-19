# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:31:09 2016

@author: ArmandoLC
"""

#Tw2_Convert2Pandas
'''
Este script solo convierte los archivos generados en script Tw1_Get_Files en formato DataFrame
'''

#Si es que es necesario convertirlo a pandas aquí está el código
#solo anote los campos que necesito. Twitter tiene más campos y campos anidados también
#es necesario correr Tw1_Get_Files.py primero
import pandas as pd
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweetx: tweetx['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
#tweets['user'] = map(lambda tweet: tweet['user'], tweeti[1])
tweets['id'] = map(lambda tweet: tweet['id'], tweets_data)
tweets['created_at'] = map(lambda tweet: tweet['created_at'], tweets_data)
tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], tweets_data)
tweets['retweeted'] = map(lambda tweet: tweet['retweeted'], tweets_data)
tweets['coordinates'] = map(lambda tweet: tweet['coordinates'], tweets_data)
tweets['hashtags'] = map(lambda tweet: tweet['entities']['hashtags'], tweets_data)
tweets['favorited'] = map(lambda tweet: tweet['favorited'], tweets_data)
tweets['id_str'] = map(lambda tweet: tweet['id_str'], tweets_data)
tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], tweets_data)
tweets['geo'] = map(lambda tweet: tweet['geo'], tweets_data)
tweets['in_reply_to_screen_name'] = map(lambda tweet: tweet['in_reply_to_screen_name'], tweets_data)
tweets['place'] = map(lambda tweet: tweet['place'], tweets_data)
