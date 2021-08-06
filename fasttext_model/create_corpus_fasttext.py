from tqdm import tqdm
import csv
import pandas as pd

def create_corpus_fasttext(train_csv: str = 'dataset/train.csv', output: str = 'corpus_fasttext.txt', train_corpus: str = 'train_details.txt'):
	'''
		This program appends the labels in the format expected by fasttext
		Arguments:
		train_csv: String which gives the path to the training csv file. It assumes the labels to be in the last column
		output: String which gives the path to the output training file.
		train_corpus: String which gives the path to the preprocessed corpus.
		
		Outputs:
		String which returns the name of the output file, ready to be trained by fasttext.

	'''
	# Reading and opening the required files
	df = pd.read_csv(train_csv)
	corpus = open(output)
	output_labels = open(train_corpus)
	label = df.keys()[-1]

	# Appending the labels to the output txt file
	for idx,line in enumerate(tqdm(corpus.readlines())):
		line = line.replace('\n','')
		output_labels.write(line + " " + "__label__" + str(df[label].iloc[idx]) + '\n')

	output_labels.close()
	corpus.close()

	return output