import gcld3
import re
from string import digits
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

def sentiment_analyzer_scores(sentence):
    '''
    VADER Sentiment used to tag the.
    Returns the predicted labels: positive/negative/neutral.

    Instantiate analyzer before running this function:
    analyzer = SentimentIntensityAnalyzer()
    '''
    analyzer = SentimentIntensityAnalyzer()

    score = analyzer.polarity_scores(sentence)

    if score['compound'] >= .05:
        sent = 'positive'
    elif score['compound'] <= -.05:
        sent = 'negative'
    else:
        sent = 'neutral'

    return sent

def unlist(x):
    return ", ".join(x)





def detect_lang(x):
    '''
    Inputs a tweet and outputs the language the tweet is in. Can be applied
    to a tweet column in order to filter out non-english tweets.
    '''

    detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, max_num_bytes=1000)

    result = detector.FindLanguage(text=x)
    return result.language


def clean_hash(text):
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())
    return text



def cleaner_text(text):
    '''takes in a string and removes lone characters, and numbers.'''
    orig_text=text
    clean_txt=''.join(c if c not in map(str,range(0,10)) else "" for c in orig_text)
    text = clean_txt

    # remove numbers from any location in a string
    remove_digits = str.maketrans('', '', digits)
    text = text.translate(remove_digits)



    text = ' '.join(re.sub('(^| ).(( ).)*( |$)'," ",text).split())
    text = text.lower()


    return text
