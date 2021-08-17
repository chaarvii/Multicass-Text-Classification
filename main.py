import os
import sys
import argparse
sys.path.append('./preprocess_text')
sys.path.append('./fasttext_model')

from create_corpus import create_corpus
from preprocess_text import preprocess_text
from create_corpus_fasttext import create_corpus_fasttext

def main(train_csv: str, test_csv: str, model_name: str, remove_html: bool, remove_digits: bool, remove_emoticons: bool, remove_stopwords: bool, lemmatise: bool):
	print('Creating the training corpus')
	create_corpus(train_csv, model_name)
	print('---')
	print('Creating fasttext corpus')
	create_corpus_fasttext(train_csv, f'dataset/{model_name}_train.txt', f'dataset/{model_name}_train_fasttext.txt', model_name)
	print('---')
	print('Creating the test corpus')
	create_corpus(test_csv, model_name, train = False)
	print('---')
	print('Preprocessing the train and test corpora')
	preprocess_text(f'dataset/{model_name}_train_fasttext.txt',f'dataset/{model_name}_train_cleaned.txt',remove_html,remove_digits,remove_emoticons,remove_stopwords, lemmatise)
	preprocess_text(f'dataset/{model_name}_test.txt',f'dataset/{model_name}_test_cleaned.txt',remove_html,remove_digits,remove_emoticons,remove_stopwords, lemmatise)
	print('---')
	os.chdir('fasttext_model/scripts')
	os.system('./build_fasttext.sh')
	print('Beginning Training')
	os.system(f'./train.sh ../../dataset/{model_name}_train_cleaned.txt ../../models/{model_name}')
	print('---')
	os.system(f'./infer.sh ../../models/{model_name}.bin ../../dataset/{model_name}_test_cleaned.txt')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--train_csv', type = str, default = 'dataset/train.csv', help =  'Path to the training csv file with labels in the last column')
	parser.add_argument('--test_csv', type = str, default = 'dataset/test.csv', help =  'Path to the testing csv file')
	parser.add_argument('--model_name', type = str, default = 'classify', help = 'Name of model being trained')
	parser.add_argument('--remove_html', action = 'store_true', help = 'Removes html tags from text')
	parser.add_argument('--remove_digits', action = 'store_true', help = 'Removes numbers from text')
	parser.add_argument('--remove_emoticons', action = 'store_true', help = 'Removes emojis from text')
	parser.add_argument('--remove_stopwords', action = 'store_true', help = 'Removes stopwords from text')
	parser.add_argument('--lemmatise', action = 'store_true', help = 'Performs lemmatisation')
	args = parser.parse_args()
	main(args.train_csv, args.test_csv, args.model_name, args.remove_html, args.remove_digits, args.remove_emoticons, args.remove_stopwords, args.lemmatise)

