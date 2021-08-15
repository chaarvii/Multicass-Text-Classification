import csv
from tqdm import tqdm
import argparse

def create_predictions(header: list = ['PRODUCT_ID', 'BROWSE_NODE_ID']):
	'''
		This functions converts the output from a fasttext model inferencing output to a csv file.
		Inputs:
		list with the header contents. This would make the first row of the output predictions.csv file

		Outputs:
		String giving the name of predictions file
	'''
	# Creating predictions.csv
	f_submissions = open('predictions.csv', 'w')
	writer = csv.writer(f_submissions)

	# Opening predictions.txt
	f_preds = open('predictions.txt')
	preds = f_preds.read().replace('__label__', '').split('\n')

	# Writing to the csv file
	writer.writerow(header)
	for idx, pred in enumerate(tqdm(preds)):
		# try:
		if pred != preds[-1]:
			writer.writerow([idx+1, int(float(pred))])
		# except:
		# 	print(f'Exception at index {idx} - Prediction was {pred}')

	f_preds.close()
	f_submissions.close()

	return 'predictions.csv'

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--header_first', type = str, default = 'PRODUCT_ID', help = 'First column heading')
	parser.add_argument('--header_second', type = str, default = 'BROWSE_NODE_ID', help = 'Second column heading')
	args = parser.parse_args()

	if args.header_first == '_' or args.header_second == '_':
		args.header_first = 'PRODUCT_ID'
		args.header_second = 'BROWSE_NODE_ID'
		
	create_predictions([args.header_first, args.header_second])