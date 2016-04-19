# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:26:32 2016

@author: ArmandoLC
"""

#Tw6_Bigrams

'''
Este script plotea los bigrams de los candidatos. No es necesario hacer tanto layout. Se puede eliminar esa parte del grafico sin problema
'''



#Corral bi-grams
sentence=no_urls_no_tags
sentence2=no_urls_no_tags2
tokens = nltk.word_tokenize(sentence)
pairs1 = [ " ".join(pair) for pair in nltk.bigrams(tokens)]
f=Counter(pairs1)
ff=f.most_common(30)

tokens2 = nltk.word_tokenize(sentence2)
pairs2 = [ " ".join(pair) for pair in nltk.bigrams(tokens2)]
f2=Counter(pairs2)
ff2=f2.most_common(30)


import numpy as np
x=[]
y=[]
l_texto=[]
long_word=[]
for i in range(0,30):
    tokensff = nltk.word_tokenize(ff[i][0])
    x.append(tokensff[0])
    y.append(tokensff[1])
    l_texto.append(ff[i][1])


for i in range(0,30):
    tokensff2 = nltk.word_tokenize(ff2[i][0])
    x.append(tokensff2[0])
    y.append(tokensff2[1])
    l_texto.append(ff2[i][1])



data = Data([
    Scatter(
        x=x,
        y=y,
        marker=Marker(
            color= np.random.randn(100),#'jet',#['rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(93, 164, 214)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(225, 144, 14)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(44, 160, 101)', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(225, 65, 54', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65', 'rgb(54, 60, 65'],
            #opacity=[1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3, 1, 0.8, 0.6, 0.4, 0.3],
            colorscale='Viridis',
        #showscale=True,
            size=l_texto
        ),
        mode='markers',
        name='y',
        text=texto
    )
])
layout = Layout(
    height=900,
    showlegend=False,
    title='Enrique Serrano y Javier Corral Most frequent BIGRAMS',
    width=900,
    xaxis=XAxis(
        title='Candidatos bigrams'
    ),
    yaxis=YAxis(
        title='BiGram Frequency'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)







x=[]
y=[]
for element in ff:
    x.append(element[0])
    y.append(element[1])


x2=[]
y2=[]
for element in ff2:
    x2.append(element[0])
    y2.append(element[1])


data = Data([
    Bar(
        x=x, #x=['app', 'appl', 'best', 'can', 'first', 'game', 'get', 'googl', 'make', 'new', 'now', 'one', 'report', 'say', 'show', 'us', 'video', 'watch', 'will', 'world'],
        y=y,#y=[1035, 1462, 935, 1173, 1014, 1329, 1498, 1541, 1458, 2979, 1113, 1105, 957, 1136, 990, 1208, 2122, 1097, 1903, 1001],
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
    title='Corral Frequent Bigrams',
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
        #ticks='outside',
        #title='bigram',
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
 


