import pandas as pd
import nltk
import re
import string
import transformers

from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from transformers import (TextClassificationPipeline)


"""
    This library contains the methods used by the API to predict review sentiment.
"""

# Definition of variables
tokenizer_name = "distilbert-base-uncased"
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

stops = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
only_english = set(nltk.corpus.words.words())

# Function definition

def correct_text(text, stem=False, lemma=False, spell=False):
    if lemma and stem:
        raise Exception('Either stem or lemma can be true, not both!')
        return text
    
    sample = text
    
    #removing stopwords
    sample = sample.lower()
    sample = [word for word in sample.split() if not word in stops]
    sample = ' '.join(sample)
    
    if lemma:
        sample = sample.split()
        sample = [lemmatizer.lemmatize(word) for word in sample]
        sample = ' '.join(sample)
        
    if stem:
        sample = sample.split()
        sample = [ps.stem(word) for word in sample]
        sample = ' '.join(sample)
    
    if spell:
        sample = str(TextBlob(text).correct())
    
    return sample


def clean_text(text):    
    sample = text
    sample = " ".join([x.lower() for x in sample.split()])
    sample = re.sub(r"\S*https?:\S*", '', sample) 
    sample = re.sub('\[.*?\]', '', sample) 
    sample = re.sub('\(.*?\)', '', sample) 
    sample = re.sub('[%s]' % re.escape(string.punctuation), '', sample) 
    sample = re.sub('\w*\d\w', '', sample)
    sample = re.sub(r'\n', ' ', sample)
    sample = re.sub(r'\\n', ' ', sample)
    sample = re.sub("[''""...“”‘’…]", '', sample)
    sample = re.sub(r', /<[^>]+>/', '', sample)
    
    sample = ' '.join([w for w in nltk.wordpunct_tokenize(sample) if w.lower() in only_english or not w.isalpha()])
    sample = ' '.join(list(filter(lambda ele: re.search("[a-zA-Z\s]+", ele) is not None, sample.split())))
    
    sample = re.compile("["
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F300-\U0001F5FF"  
                               u"\U0001F680-\U0001F6FF"  
                               u"\U0001F1E0-\U0001F1FF"  
                               u"\U00002500-\U00002BEF"  
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  
                               u"\u3030"
                               "]+", flags=re.UNICODE).sub(r'', sample) 
    sample = sample.strip()
    sample = " ".join([x.strip() for x in sample.split()])
    
    return sample   


def predict_sentiment(r: str):
    tokenizer = transformers.DistilBertTokenizerFast.from_pretrained(tokenizer_name)
    trn = transformers.DistilBertForSequenceClassification.from_pretrained(model_name).cpu()
    pipe = TextClassificationPipeline(model=trn, tokenizer=tokenizer, return_all_scores=True)
    
    return pipe(r)



