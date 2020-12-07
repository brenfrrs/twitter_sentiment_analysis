#!/usr/bin/env python3

import keyboard
import pandas as pd
import numpy as np
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

'''

This script can be used to tag tweets quickly as positive/negative/neutral.

press Y for "positive"
press N for "negative"
press space for "neutral"
press x to skip a tweet


'''



print('imported packages \n')

main_df = pd.read_csv('apple_goog.csv', index_col=0)
main_df = main_df.drop_duplicates(subset='c_tweet', keep="first")

tagged_data = pd.read_csv('tagged.csv',index_col=0)

print('LOADED DATA')


counter = 0

#instantiate analyzer
analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)

    if score['compound'] >= .05:
        #positive sentiment
        print('\033[92m' + sentence + '\033[00m')


    elif score['compound'] <= -.05:
        #negative sentiment
        print('\033[91m' + sentence + '\033[00m')


    else:
        #neutral
        print('\033[97m' + sentence + '\033[00m')




while True:
    sentiment_analyzer_scores(main_df.iloc[counter][7])
    if keyboard.is_pressed('y'):
        tagged_data = tagged_data.append({'message':main_df.iloc[counter][7], 'positive':1, 'negative':0, 'neutral':0}, ignore_index=True)
        tagged_data.to_csv('tagged.csv')
        counter +=1
        print('Positive', counter)
        time.sleep(.2)

    elif keyboard.is_pressed('n'):
        tagged_data = tagged_data.append({'message':main_df.iloc[counter][7], 'positive':0, 'negative':1, 'neutral':0}, ignore_index=True)
        tagged_data.to_csv('tagged.csv')
        counter += 1
        print('Negative', counter)
        time.sleep(.2)

    elif keyboard.is_pressed('space'):
        tagged_data = tagged_data.append({'message':main_df.iloc[counter][7], 'positive':0, 'negative':0, 'neutral':1}, ignore_index=True)
        tagged_data.to_csv('tagged.csv')
        counter += 1
        print('NEUTRAL')
        time.sleep(.2)

    elif keyboard.is_pressed('esc'):
        print('ESCAPE PRESSED SKIP ENTRY')
        counter+=1
        time.sleep(.2)
        break

    elif keyboard.is_pressed('x'):
        print('SKIPPING to {}'.format(counter))
        counter += 1
        time.sleep(.12)
