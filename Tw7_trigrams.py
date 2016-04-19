# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:34:18 2016

@author: ArmandoLC
"""

#Tw7_trigrams 

from nltk.util import ngrams
text_trigram = sentence
token=nltk.word_tokenize(text_trigram)
#tokens = nltk.word_tokenize(sentence)
triplets1 = [ " ".join(three) for three in nltk.ngrams(token,3)]
ftri=Counter(triplets1)
fftri=ftri.most_common(30)
#trigrams=ngrams(token,3)

from nltk.util import ngrams
text_trigram2 = sentence2
token2=nltk.word_tokenize(text_trigram2)
#tokens = nltk.word_tokenize(sentence)
triplets2 = [ " ".join(three) for three in nltk.ngrams(token2,3)]
ftri2=Counter(triplets2)
fftri2=ftri2.most_common(30)

x=[]
y=[]
for element in fftri:
    x.append(element[0])
    y.append(element[1])


x2=[]
y2=[]
for element in fftri2:
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
    title='Corral Frequent trigrams',
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
