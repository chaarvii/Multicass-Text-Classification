import pandas as pd
from tqdm import tqdm
from collections import Counter

def create_corpus(train_csv: str = '../dataset/train.csv') -> str:
	'''
		This function converts the input csv file(with multiple features in different columns and a label in the last column) 
		into a txt file with each line as one entry. The multiple features are concatenated together
		Arguments:
		train_csv: The path of the training csv file, relative to the create_corpus.py

		Outputs:
		Returns a string which has the name of the created txt file. The file is located in the same directory as your input csv file.
	'''
	# Reading train_csv
	df = pd.read_csv(train_csv)

	# Creation of output file
	corpus_folder = train_csv.split('/')
	corpus_name = ''

	for folder in corpus_folder:
		if folder == corpus_folder[-1]:
			break
		else:
			corpus_name += folder +'/'

	corpus_name += train.txt
	f_corpus = open('train.txt', 'a')

	# Appending the entries in the output file
	label = df.keys()[-1]
	for x in tqdm(range(len(df))):
	corpus = ''
	for y in df.keys():

		# Break out if we are at the last column
		if y == label:
			break

		# To handle entries which are NaN	
		if not isinstance(df.iloc[x][y], str):
			continue
		else:
			corpus += str(df.iloc[x][y]) + ' '
		corpus += '\n'
	f_corpus.write(corpus)
	# To manage RAM with large corpora
	del corpus

	# Completed creation of corpus
	f_corpus.close()
	return 'train.txt'