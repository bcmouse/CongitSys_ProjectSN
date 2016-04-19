# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:09:39 2016

@author: ArmandoLC
"""

#Tw5_Frequency_words

#################################################################################
########## EN ESTA SECCION SE PLOTEAN LAS PALABRAS MAS FRECUENTES DE CADA CANDIDATO
####################################################################################
import plotly.plotly as py
from plotly.graph_objs import *
#py.sign_in('username', 'api_key')
#Necesitan instalar plotly, tiene costo. Te deja hacer una cantidad de graficos al día. Son bastantes según recuerdo


from collections import Counter
word_counts = sorted(Counter(words_Corral).values(), reverse=True)

plt.loglog(word_counts)
plt.ylabel("Freq")
plt.xlabel("Word Rank")
########################333
from collections import Counter
words_sep=words_Corral.split()
for item in [words_sep]:
    c = Counter(item)
    print c.most_common()[:10] # top 10
    print


#solo cuenta las frecuencias de cada palabra en la lista
STOPWORDS2=[x.strip() for x in open('C:\\Users\\ArmandoLC\\AppData\\Roaming\\nltk_data\\corpora\\stopwords\\spanish').read().split('\n')]
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
#s0 = tweets['text'][0]
s0 = words_Serrano
tknzr.tokenize(s0)
words_sep=tknzr.tokenize(s0)
words_lower = [w.lower() for w in words_sep]


non_stop_words = filter(lambda x: x not in STOPWORDS2, words_lower)
no_urls_no_tags = " ".join([word for word in non_stop_words
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'rt'
                                and word.isalpha()   #quito lossignos de puntuacion
                            ])

words_sep=no_urls_no_tags.split()
for item in [words_sep]:
    c = Counter(item)
    print c.most_common()[:50] # top 10
    print
Most_freq=c.most_common()[:50]

Most_freq_C=c.most_common()[:50]

x=[]
y=[]
for element in Most_freq:
    x.append(element[0])
    y.append(element[1])


####NOTA: No es necesario poner un layout, plotly te da uno por default, pero yo si lo puse de cualquier forma

data = Data([
    Bar(
        x=x, 
        y=y,
        marker=Marker(
            color='rgb(51,153,255)',
            line=Line(
                color='rgb(0, 0, 0)',
                width=1
            )
        ),
        showlegend=False,
        uid='126dca',
        xaxis='x',
        yaxis='y'
    )
])
layout = Layout(
    autosize=True,
    barmode='stack',
    height=555,
    legend=Legend(
        x=1.05,
        y=0.5,
        bgcolor='rgb(255,255,255)',
        bordercolor='transparent',
        font=Font(
            family=''
        ),
        xanchor='center',
        yanchor='top'
    ),
    margin=Margin(
        r=10
    ),
    paper_bgcolor='rgb(255,255,255)',
    plot_bgcolor='rgb(229,229,229)',
    showlegend=False,
    title='Most Frequent Words In Serrano-Related Tweets',
    titlefont=dict(
        family=''
    ),
    width=927,
    xaxis=XAxis(
        autorange=True,
        gridcolor='rgb(255,255,255)',
        range=[-0.5, 19.5],
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        title='Word',
        type='category',
        zeroline=False
    ),
    yaxis=YAxis(
        autorange=True,
        gridcolor='rgb(255,255,255)',
        range=[0, 3135.7894736842104],
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        title='Frequencies',
        type='linear',
        zeroline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)