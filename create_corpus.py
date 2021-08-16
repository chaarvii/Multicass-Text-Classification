import csv
import os
import pandas as pd
from tqdm import tqdm
from collections import Counter

def create_corpus(train_csv, model_name, train = True):
	'''
		This function converts the input csv file(with multiple features in different columns and a label in the last column) 
		into a txt file with each line as one entry. The multiple features are concatenated together
		Arguments:
		train_csv: The path of the training csv file, relative to the create_corpus.py

		Outputs:
		None
	'''
	# Reading train_csv
	df = pd.read_csv(train_csv, escapechar = "\\", quoting = csv.QUOTE_NONE)
	corpus_name = f'dataset/{model_name}_train.txt' if train else f'dataset/{model_name}_test.txt'
	os.system(f'rm {corpus_name}')
	f_corpus = open(corpus_name, 'a')

	# Appending the entries in the output file
	label = df.keys()[-1]
	for x in tqdm(range(len(df))):
		corpus = ''
		for y in df.keys():

			# Break out if we are at the last column
			if train:
				if y == label:
					break
					
			# To handle entries which are NaN	
			if isinstance(df.iloc[x][y], float):
				continue
			else:
				corpus += str(df.iloc[x][y]) + ' '
		corpus += '\n'
		f_corpus.write(corpus)
		# To manage RAM with large corpora
		del corpus

	# Completed creation of corpus
	f_corpus.close()