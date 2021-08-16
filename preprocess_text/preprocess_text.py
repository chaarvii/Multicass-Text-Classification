from tqdm import tqdm
import csv
import pandas as pd
import argparse

def preprocess_text(input_file:str,output_file:str,remove_html_tag:bool,remove_digit:bool,remove_emoticon:bool,remove_stopwords:bool,lemmatise:bool):
    '''
            This function performs text preprocessing on the data. 
            The workflow is as follows:
            1. Convert text to lowercase
            2. Remove punctuation 
            3. Remove html tags (optional)
            4. Remove numbers (optional)
            5. Remove emoji (optional)
            6. Lemmatisation and Stemming (optional)
            7. Remove Stopwords (optional)
            Arguments:
            input_file: string which has the path to .txt file containing data to be preprocessed in fasttext format
            output_file: string which has the path to .txt file for storing cleaned data
            remove_html_tag: boolean, if true, html tags are removed from the data 
            remove_digit: boolean, if true, numbers are removed from the data 
            remove_emoticon: boolean, if true, emojis are removed from the data
            remove_stopwords: boolean,if true, stopwords are removed from the data 
            lemmatise: boolean,if true, lemmatisation is done

            Output:
            output_file: String which returns the name of the output file, ready for training
    '''
    # Reading and opening the required files
    f_train = open(input_file)
    print("Read {}".format(input_file))
    train = f_train.readlines()
    file = open(output_file,'a')

    #preprocessing pipeline
    for i, x in enumerate(tqdm(train)):
        line = x
        data = line.rsplit(' ', 1)[0]
        label = line.rsplit(' ',1)[1]
        data = clean_text(data,remove_html_tag)
        if remove_digit == True:
            data = remove_numbers(data)
        if remove_emoji == True:
            data = remove_emoji(remove_emoticon)

        if lemmatise == True:
            data = lemmatise_text(data,remove_stopwords)
        elif remove_stopwords == True:
            data = remove_stopwords(data)

        #Appending processed text to output file
        file.write(data)
    file.close()
    f_train.close()
    return output_file

if __name__ == '__main__':
	    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	    parser.add_argument('--input', type = str, default = 'dataset/train.txt', help = 'Path to the text file in fasttext format')
	    parser.add_argument('--output', type = str, default = 'cleaned_text.txt', help = 'Path to the output file')
	    parser.add_argument('--remove_html', type = bool, default = True, help = 'removes html tags from text, True by default')
    	parser.add_argument('--remove_digit', type = bool, default = True, help = 'removes numbers from text, True by default')
    	parser.add_argument('--remove_emoticon', type = bool, default = True, help = 'removes emojis from text, True by default')
    	parser.add_argument('--remove_stopwords', type = bool, default = True, help = 'removes stopwords from text, True by default')
        parser.add_argument('--lemmatise', type = bool, default = True, help = 'performs lemmatisation, True by default')
    	args = parser.parse_args()

    	preprocess_text(args['input'], args['output'], args['remove_html'],args['remove_digit'],args['remove_digit'],args['remove_emoticon'],args['remove_stopwords'],args['lemmatise'])
