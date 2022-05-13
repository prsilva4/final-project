
import re

def clean_up(s):
    
    lower = s.lower()
    no_url = re.sub('http\S+', '', lower)
    str_list = re.findall('[a-z]+', no_url)          
    
    return ' '.join(str_list)



import nltk
nltk.download('punkt')

def tokenize(s):
    return nltk.word_tokenize(s)


from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import*
nltk.download('wordnet')

def stem_and_lemmatize(l):
    
    lem_stem_list = [] 
    
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    for word in l:
        lem = lemmatizer.lemmatize(word)
        stem = stemmer.stem(lem)
        lem_stem_list.append(stem)
    
    return lem_stem_list


from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))


def remove_stopwords(l):    
    
    filtered_sentence = [w for w in l if not w in stop_words]
    
    return filtered_sentence


def all_in_one(new_input):
    
    new_input=clean_up(new_input)
    new_input=tokenize(new_input)
    new_input=stem_and_lemmatize(new_input)
    new_input=remove_stopwords(new_input)
    
    return new_input





