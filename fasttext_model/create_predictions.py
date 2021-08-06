import csv
from tqdm import tqdm

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
		try:
			writer.writerow([idx+1, int(pred)])
		except:
			print(f'Exception at index {idx} - Prediction was {pred}')

	f_preds.close()
	f_submissions.close()

	return 'predictions.csv'