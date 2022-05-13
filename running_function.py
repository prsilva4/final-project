
from all_in_one import all_in_one

def running(tweet):
    
    import pickle
    with open('dicionario.pickle', 'rb') as handle:
        
        dicionario = pickle.load(handle)
    
        new_tweet = all_in_one(tweet) # tratando o novo tweet
    
        dicionario2 = dicionario.copy() # copiando o bag of words

        words_in_common = list(set(list(dicionario2.keys())).intersection(set(new_tweet))) # intersection
    try:
        for word in words_in_common: # iterando todas as palavras em comum
            if word in dicionario2.keys(): # avaliando se a palavra em comum esta no bow
                dicionario2[word] = True # se estiver muda o bow para true nesta palavra
                
        return dicionario2 # retorna o bow modificado
    
    except:
        return dicionario2 # retorna o bow original    


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
