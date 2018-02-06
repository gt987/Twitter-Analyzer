from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd
import numpy as np

import re, string
def tokenize(text):
    return re.sub(ur"\p{P}+", "", text).split()



def toxicity(twitter_account_input):
    #vec = joblib.load('models/vec.pkl')
    #label_cols = ['Toxic', 'Obscene', 'Threating', 'Insulting', 'Racist']
    #twitter_account = twitter_account_input
    #twitter_term_doc = vec.transform(twitter_account['text'])
    #preds = np.zeros((len(twitter_account), len(label_cols)))

    #for i, j in enumerate(label_cols):
    #    m,r = joblib.load('models/' + j +'.pkl')
    #    preds[:,i] = m.predict_proba(twitter_term_doc.multiply(r))[:,1]

    #toxicity = pd.DataFrame(preds, columns = label_cols)
    #toxicity_vals = toxicity.describe()

    #scale = ['Mildly ', '','Extremely ']
    #notable_tweets = []

    #for col in list(toxicity.columns.values):
    #    tweet_id = toxicity[col].idxmax()
    #    val = toxicity[col].iloc[tweet_id]
    #    if val>=0.25:
    #        #notable_tweets.append(scale[int(4*val)]+col+": "+twitter_account.loc[tweet_id]['text'].decode('utf8').encode('ascii', errors='ignore'))
    #        notable_tweets.append({'category': scale[int(4*val)]+col, 'text': twitter_account.loc[tweet_id]['text'].decode('utf8').encode('ascii', errors='ignore')})
    #return toxicity_vals.loc[['mean','max']], notable_tweets
    return 'test', [twitter_account_input['text'].loc[0]]
