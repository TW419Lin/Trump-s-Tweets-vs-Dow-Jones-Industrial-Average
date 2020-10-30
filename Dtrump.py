#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:24:12 2020

@author: muselin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tweets = pd.read_csv('BeforeCovid.csv')
tweets.columns = ['date1', 'tweets', 'date2', 'DJI']

tweet_date = tweets['date1'].tolist()
Dtweets = tweets['tweets'].tolist()
dji_date = tweets['date2'].tolist()
DJI = tweets['DJI'].tolist()

new_date = list()
daily_tweets = list()
daily_DJI = list()
total_tweets = list()
for i in dji_date:
    for r in tweet_date:
        if i == '2020/03/23':
            break
        elif i == r:
            new_date.append(i)
            index = dji_date.index(i)
            daily_DJI.append(DJI[int(index)])
            daily_tweets.append(abs(Dtweets[index+1]-Dtweets[index]))
            total_tweets.append(Dtweets[index])

plt.plot(total_tweets,daily_DJI)
plt.plot(daily_tweets,daily_DJI)


new_date = np.array(new_date)
daily_tweets = np.array(daily_tweets)
daily_DJI = np.array(daily_DJI)
total_tweets = np.array(total_tweets)

df = pd.DataFrame({'date': new_date,
                    'tweets': daily_tweets,
                    'total tweets': total_tweets,
                    'dji': daily_DJI})

df.to_csv('TrumpDF.csv')
result = df.corr('pearson')
print(result['dji'])

