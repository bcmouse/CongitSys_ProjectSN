# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:36:43 2016

@author: ArmandoLC
"""

#Tw3_WordCloud

'''
Este script solo crea una nube de palabras utilizando la librería WordCloud, existen varias librerías de wordCloud
o formas de hacerlo.

Se hace uso de DataFrames por lo que los tweets deben estar en formato de DataFrame, es por eso que se debe correr
primero el script Tw2_Convert2Pandas
'''

#harcode de stopwords en español para usarlo en la librería, por que el que trae por default está en inglés
STOPWORDS=set([x.strip() for x in open('C:\\Users\\ArmandoLC\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\spanish').read().split('\n')])


words = ' '.join(tweets['text'])  #para obtener las palabras del campo 'text' de twitter

# remove URLs, RTs, and twitter handles
no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

wordcloud = WordCloud(
                      stopwords=STOPWORDS,
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(no_urls_no_tags)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./my_twitter_wordcloud_1.png', dpi=300)
plt.show()

#Nota words.split es equivalente a utilizar la librería tokenizer de nltk
