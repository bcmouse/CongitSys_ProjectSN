# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:49:31 2016

@author: ArmandoLC
"""

#Tw4_Get_WordRelated_Tweet
'''
Rutina para extraer tweets relacionados a un candidato
'''
##########################################################################33
#En esta seccion se extraen los tweets relacionados a los candidatos
#solo es una búsqueda simple (no exhaustiva porque el set de datos es pequeño)
#se puede hacer más exacta con operadores logicos
###############################################################################
import re
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
    
tweets['Corral'] = tweets['text'].apply(lambda tweet: word_in_text('corral', tweet))
Related_to_Corral=tweets['text'][tweets['Corral']==True]
tweets['Serrano'] = tweets['text'].apply(lambda tweet: word_in_text('serrano', tweet))
Related_to_Serrano=tweets['text'][tweets['Serrano']==True]
tweets['Serrano2'] = tweets['text'].apply(lambda tweet: word_in_text('serrano', tweet) and word_in_text('corral', tweet))
Related_to_Serrano2=tweets['text'][tweets['Serrano2']==True]

tweets['Pbis'] = tweets['text'].apply(lambda tweet: word_in_text('Pbis', tweet))
Related_to_Pbis=tweets['text'][tweets['Pbis']==True]


### Si se quiere plotear la nube de palabras de los candidatos


#words_Serrano = ' '.join(Related_to_Serrano)  #para obtener las palabras
#no_urls_no_tags_Serrano = " ".join([word for word in words_Serrano.split()
#                            if 'http' not in word
#                                and not word.startswith('@')
#                                and word != 'RT'
#                            ])
#
#wordcloud_Serrano = WordCloud(
#                      #font_path='/Users/sebastian/Library/Fonts/CabinSketch-Bold.ttf',
#                      stopwords=STOPWORDS,
#                      background_color='black',
#                      width=1800,
#                      height=1400
#                     ).generate(no_urls_no_tags_Serrano)
#
#plt.imshow(wordcloud_Serrano)
#plt.axis('off')
#plt.savefig('./Serrano_WordCloud.png', dpi=300)
#plt.show()