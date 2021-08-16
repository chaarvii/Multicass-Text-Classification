import numpy as np
from tqdm import tqdm
import random
import re
import spacy
from spacy.lang.en import STOP_WORDS
from spacy.lang.en import English
nlp = English()
stops = STOP_WORDS

def lemmatise_text(product_detail:str,remove_stopwords:bool):
    '''
            This function performs the following tasks:
            1. Stemming and Lemmatisation
            2. Removes stop words (optional)
            Arguemts:
            product_detail: String contating product details and labels. 
            It assumes that the input is according to fasttext format.
            remove_stopwords: boolean value, if True removes stopwords
            from the text. 

            Output:
            cleaned string in fasttext format
    '''
    # tokenising the text 
    tokenizer = nlp.Defaults.create_tokenizer(nlp)
    tokens = tokenizer(product_detail)
    lemmatized = list()

    # performing lemmatisation and stemming, removing stopwords if true
    for word in tokens:
        lemma = word.lemma_.strip()
        if lemma:
            if not remove_stopwords or (remove_stopwords and lemma not in stops):
                lemmatized.append(lemma)

    #converting list back to string
    return " ".join(lemmatized)
