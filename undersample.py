import pandas as pd
import csv
import numpy as np
from tqdm import tqdm
import random
from collections import Counter


def load_data(filePath):
    '''
    Input: data file path 

    This function creates a dataframe and a dictionary of unique label counts 

    Output: Dataframe, Dictionary
    '''
    print('Reading CSV')
    df = pd.read_csv(filePath, escapechar = "\\", quoting = csv.QUOTE_NONE)
    nodes = list(df['BROWSE_NODE_ID'])
    nodes_dist = dict(Counter(nodes))
    return df,nodes_dist

def undersample(df,threshold,probability_threshold):
    '''
    Input: Dataframe, undersampling threshold, undersampling probability

    This function undersamples the data and creates a new txt file with modified data 

    Output: None
    '''
    file = open('train_details_undersampled.txt', 'a')
    for i in tqdm(range(len(df))):
        browse_node = int(df['BROWSE_NODE_ID'].iloc[i])
        if nodes_dist[browse_node] > threshold:
            prob = random.random()
            if prob > probability_threshold:
                continue
        file.write(train[i])

    file.close()