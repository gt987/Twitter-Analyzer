from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from tokenizer import my_tok
import string
import pandas as pd
import numpy as np

vec = joblib.load('/home/gt987/Twitter-Analyzer/models/vec.pkl')
label_cols = ['Toxic', 'Obscene', 'Threatening', 'Insulting', 'Racist']

def toxicity(tweets_df):
    tweets_df['text'].fillna("unknown", inplace=True)
    twitter_term_doc = vec.transform(tweets_df['text'])
    preds = np.zeros((len(tweets_df), len(label_cols)))

    for i, j in enumerate(label_cols):
        m,r = joblib.load('/home/gt987/Twitter-Analyzer/models/' + j +'.pkl')
        preds[:,i] = m.predict_proba(twitter_term_doc.multiply(r))[:,1]

    toxicity = pd.DataFrame(preds, columns = label_cols)
    toxicity_vals = toxicity.describe()

    scale = ['Mildly ', '','Extremely ']
    notable_tweets = []

    for col in list(toxicity.columns.values):
        tweet_id = toxicity[col].idxmax()
        val = toxicity[col].iloc[tweet_id]
        if val>=0.25:
            notable_tweets.append({'category': scale[int((val-0.25)/0.251)]+col, 'text': tweets_df.loc[tweet_id]['text'].decode('utf8').encode('ascii', errors='ignore')})
    return toxicity_vals.loc[['mean','max']], notable_tweets


