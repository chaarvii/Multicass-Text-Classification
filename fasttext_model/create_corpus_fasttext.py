from tqdm import tqdm
import csv
import pandas as pd
import argparse

def create_corpus_fasttext(train_csv, train_corpus, output):
	'''
		This program appends the labels in the format expected by fasttext
		Arguments:
		train_csv: String which gives the path to the training csv file. It assumes the labels to be in the last column.
		output: String which gives the path to the output training file.
		train_corpus: String which gives the path to the preprocessed corpus.
		
		Outputs:
		String which returns the name of the output file, ready to be trained by fasttext.

	'''
	# Reading and opening the required files
	df = pd.read_csv(train_csv, escapechar = "\\", quoting = csv.QUOTE_NONE)
	corpus = open(train_corpus)
	output_labels = open(output, 'a')
	label = df.keys()[-1]
	lines = corpus.readlines()
	print(lines[-1])

	# Appending the labels to the output txt file
	for idx,line in enumerate(tqdm(lines)):
		line = line.replace('\n','')
		output_labels.write(line + " " + "__label__" + str(df[label].iloc[idx]) + '\n')

	output_labels.close()
	corpus.close()

	return output

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--csv', type = str, default = 'dataset/train.csv', help = 'Path to the csv file with labels')
	parser.add_argument('--corpus', type = str, default = 'corpus_fasttext.txt', help = 'Path to the corresponding corpus file')
	parser.add_argument('--output', type = str, default = 'train_details.txt', help = 'Path to the output file')
	args = parser.parse_args()

	create_corpus_fasttext(args.csv, args.corpus, args.output)
