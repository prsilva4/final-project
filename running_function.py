
from all_in_one import all_in_one

def running(tweet):
    
    import pickle
    with open('dicionario.pickle', 'rb') as handle:
        
        dicionario = pickle.load(handle)
    
        new_tweet = all_in_one(tweet) 
    
        dicionario2 = dicionario.copy()

        words_in_common = list(set(list(dicionario2.keys())).intersection(set(new_tweet)))
    try:
        for word in words_in_common: 
            if word in dicionario2.keys(): 
                dicionario2[word] = True 
                
        return dicionario2 
    
    except:
        return dicionario2     


def final(newtweet):
    
    import pickle
    with open('classifier.pickle', 'rb') as handle:        
        classifier = pickle.load(handle)
    newtweet=running(newtweet)
    newtweet=classifier.classify(newtweet)
    
    if newtweet==1:
        return 'This is a disaster tweet'
    else:
        return 'This is not a disaster tweet' 
