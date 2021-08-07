import pandas as pd
import csv
import numpy as np
from tqdm import tqdm
import random
from collections import Counter


def load_data(filePath:str):
    '''
            This function creates a dataframe and a dictionary of unique label counts.
            Arguments:
            filePath: path to csv file containing the data. 

            Output:
            df: Dataframe for the csv file
            nodes_dist: dictionary containing the count of distinct labels.
    '''
    print('Reading CSV')
    df = pd.read_csv(filePath, escapechar = "\\", quoting = csv.QUOTE_NONE)
    nodes = list(df['BROWSE_NODE_ID'])
    nodes_dist = dict(Counter(nodes))
    return df,nodes_dist

def undersample(df,threshold:int,probability_threshold:float):
    '''
            This function undersamples the data and creates a new txt file with modified data 
            Arguments: 
            df: dataframe containing the data 
            threshold: decides the max number of samples a class can have
            probability_threshold: helps in deciding undersampling frequency
            
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
    return