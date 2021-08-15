from tqdm import tqdm
import numpy as np
import argparse
def ensemble(n_models):
	'''
		This model creates a predictions.txt from all the prediction files created. It can work with any number of prediction files created and with any number of predictions(n-best) made.
		Arguments:
		n_models: The number of models being ensembled

		Outputs:
		None
	'''
	# predictions list contains as many lists as number of models. Each list has the predictions for one of the models
	predictions = []
	for i in range(0, n_models):
		f = open('predictions_' + str(i + 1) + '.txt')
		predictions.append(f.readlines())
		f.close()
	output_file = open('predictions.txt', 'a')
	# Looping over each test case
	for i in tqdm(range(len(predictions[0]))):
		
		current_preds = []
		# Looping over a prediction from each model
		for p in range(n_models):
			preds = predictions[p][i].replace('__label__', '').replace('\n', '')
			current_preds.append(preds)

		preds = []
		probs = []
		# Breaking up all the predictions into predictions and probabilities
		current_preds_len = len(current_preds)
		for j in range(current_preds_len):
			current_preds[j] = current_preds[j].split(' ')
			for k in range(len(current_preds[j])):
				if k % 2 == 0:
					preds.append(float(current_preds[j][k]))
				else:
					probs.append(float(current_preds[j][k]))

		probs = np.array(probs)
		preds = np.array(preds)
		max = np.argsort(-probs)[0]
		output_file.write(str(preds[max]) + '\n')

	output_file.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--models', type = int, required = True, help = 'The number of models being ensembled')
	args = parser.parse_args()

	ensemble(args.models)

