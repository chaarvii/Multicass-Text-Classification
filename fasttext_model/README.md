# FastText
FastText is a module provided by Facebook Research. More information about the module can be find in their GitHub repository(https://github.com/facebookresearch/fastText) and on their website(https://fasttext.cc). Our repository gives an upper level API that allows one to work with the fastText text classifcation model. We provide an API to generate the required files, train and infer from the model on your own data. 

The text classifier can handle large amounts of data with short training times. It can also handle a large number of output classes.

This code was used in the Amazon ML Challenge 2021(https://www.hackerearth.com/challenges/competitive/amazon-ml-challenge/), hosted by HackerEarth, to achieve a rank of 64 from 518 submitted models.

## Installation and Setup

The following code should be run in order to initialise the different scripts.

```bash
pip install -r requirements.txt
chmod +x init.sh
./init.sh
```

## Scripts
This section will discuss the function of all the scripts, their inputs and how to use them.

### scripts/build_fasttext.sh
This script is used to clone into the fastText repository and create all the executables. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
cd scripts
./build_fasttext.sh
```

It creates a ```fastText``` directory.

### init.sh
This script initialises all the other scripts and builds the fasttext module. This should be run at intialisation as mentioned above.

### scripts/train.sh
This script trains a fasttext model. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
cd scripts
./train.sh path_to_corpus.txt path_to_save_model
```

It creates two files - ```path_to_save_model.bin``` and ```path_to_save_model.vec```. ```path_to_save_model.bin``` is the trained model and ```path_to_save_model.vec``` are embeddings for all the words in the corpus.

More options will be soon added to the script.

### scripts/infer.sh
This script can be used to infer from a trained fasttext model. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
cd scripts
./infer.sh path_to_trained_model path_to_test_corpus.txt
```

It creates a ```predictions.csv``` with all the predictions for each input case along with a serial number. It also creates an intermediate file called```predictions.txt``` which is deleted once the csv file is created.

### create_corpus_fasttext.py
This script concatenates the label with input features in the format required by fasttext. It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
python create_corpus_fasttext.py --csv path_to_csv_file --corpus path_to_corpus.txt --output path_to_output_file.txt
```

It creates a ```path_to_output_file.txt``` file which contains the corpus ready to be fed into fasttext.

Note: The aforementioned flags are optional. For more information, run ```python create_corpus_fasttext.py --help```.

### create_predictions.py
This script creates the ```predictions.csv``` from a ```predictions.txt``` . It is automatically called in the pipeline, however, if required, it can be run individually. The following format is to be used while executing it:

```bash
python create_predictions.py --header_first first_column_heading --header_second second_column_heading
```

It creates a ```predictions.csv``` with all the predictions for each input case along with a serial number.

Note: The aforementioned flags are optional. For more information, run ```python create_predictions.py --help```.
