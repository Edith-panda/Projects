#Step 1:
#importing  all the libraries
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import string
import warnings
warnings.filterwarnings("ignore", category = DeprecationWarning)
%matplotlib inline

#step 2 :
#training ans testing using twitter sentiment analysis dataset
train = pd.read_csv("https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv")
train_original = train.copy()
test = pd.read_csv("https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv")
test_original = test.copy()
combine = train.append(test , ignore_index=True, sort =True)
print(combine.head())
print(combine.tail())

#step3:
#removing unnecessary stuffs such as user id which does not contribute to output 0s and 1s
def remove_pattern(text, pattern):
  r = re.findall(pattern , text)
  for i in r:
    text = re.sub(i, "",text)
    return text
combine['Tidy_Tweets'] = np.vectorize(remove_pattern)(combine['tweet'], "@[\w]*")
combine.head()

#step4:
#Further replacing punctuatio , numbers , special characters which does not contribute in output
combine['Tidy_Tweets'] = (combine['Tidy_Tweets'].str.replace("[^a-zA-Z#]", " "))
combine.head(10)
#removing chracters less than 3 such as hmm , umm, is , was, are 
combine['Tidy_Tweets'] = combine['Tidy_Tweets'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
combine.head(10)
tokenized_tweet = combine['Tidy_Tweets'].apply(lambda x: x.split())
tokenized_tweet.head(10)

#Stemming is a rule-based process of stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from a word.
from nltk import PorterStemmer
ps = PorterStemmer()
tokenized_tweet = tokenized_tweet.apply(lambda x: [ps.stem(i) for i in x])
tokenized_tweet.head()

for i in range(len(tokenized_tweet)):
  tokenized_tweet[i] =  ' '.join(tokenized_tweet[i])
  combine["Tidy_Tweets"] = tokenized_tweet
  combine.head() 