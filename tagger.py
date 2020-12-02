#!/usr/bin/env python3

import keyboard
import pandas as pd
import numpy as np
import time



print('imported packages \n')

main_df = pd.read_csv('apple_goog.csv', index_col=0)
main_df = main_df.drop_duplicates(subset='c_tweet', keep="first")

tagged_data = pd.DataFrame(columns=['message', 'positive', 'negative', 'neutral'])

print('LOADED DATA')


counter = 0

while True:
    print(main_df.iloc[counter][7])
    if keyboard.is_pressed('y'):
        tagged_data = tagged_data.append({'message':main_df.iloc[counter][7], 'positive':1, 'negative':0, 'neutral':0}, ignore_index=True)
        tagged_data.to_csv('tagged.csv')
        counter +=1
        print('yes', counter)
        time.sleep(.2)
    
    elif keyboard.is_pressed('n'):
        tagged_data = tagged_data.append({'message':main_df.iloc[counter][7], 'positive':0, 'negative':1, 'neutral':0}, ignore_index=True)
        tagged_data.to_csv('tagged.csv')
        counter += 1
        print('no', counter)
        time.sleep(.2)

    elif keyboard.is_pressed('space'):
        tagged_data = tagged_data.append({'message':main_df.iloc[counter][7], 'positive':0, 'negative':0, 'neutral':1}, ignore_index=True)
        tagged_data.to_csv('tagged.csv')
        counter += 1
        print('SPACEEEEEEEE')
        time.sleep(.2)

    elif keyboard.is_pressed('esc'):
        print('ESCAPE PRESSED SKIP ENTRY')
        counter+=1
        time.sleep(.2)
        break

