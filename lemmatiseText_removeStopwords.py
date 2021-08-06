import numpy as np
from tqdm import tqdm
import random
import re
import spacy
from spacy.lang.en import STOP_WORDS
nlp = spacy.load("en")
stops = STOP_WORDS

def preprocess_text(product_detail,remove_stopwords):
    '''
    Input: Text to be cleaned (String), option to remove stopwords (Boolean)

    This function performs the following tasks:
    1. Stemming and Lemmatisation
    2. Removes stop words (optional)

    Output: String
    '''
    tokenizer = nlp.Defaults.create_tokenizer(nlp)
    tokens = tokenizer(product_detail)
    lemmatized = list()
    for word in product_detail:
        lemma = word.lemma_.strip()
        if lemma:
            if not remove_stopwords or (remove_stopwords and lemma not in stops):
                lemmatized.append(lemma)
    return " ".join(lemmatized)