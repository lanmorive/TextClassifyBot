import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


# noinspection PyInterpreter
def chist(df):
    result = re.sub('<br /><br />|[!.,?\-\(\):]',' ',df).lower()
    reb = re.sub(r'\s+', ' ', result)
    return reb

def delt_stop_words(text):
    words = set(stopwords.words('english'))
    return ' '.join([i for i in text.split(' ') if i not in words])

def lemma(text):
    lem = WordNetLemmatizer()
    return " ".join([lem.lemmatize(i,pos='v') for i in text.split(' ')])