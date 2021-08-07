# Text Preprocessing  

The machine learning algorithms do not comprehend unstructured text data, and thus there is a need to clean and preprocess the data so that it can be used efficiently in various NLP algorithms. Sometimes unstructured text data contains noise that needs to be treated as well. This module standardizes the text data, thus making it ready for training. The module has been made flexible, keeping in mind the broad array of NLP tasks. 

This code was used in the Amazon ML Challenge 2021(https://www.hackerearth.com/challenges/competitive/amazon-ml-challenge/), hosted by HackerEarth, to achieve a rank of 64 from 518 submitted models.

### preprocess_text.py

This script removes noise from the data and preprocesses it, thus making it ready for training. It is automatically called in the pipeline however it can be customised according to your needs with the help of the given script 

```bash
python preprocess_text.py --input path_to_input_file --output path_to_output_file.txt --remove_html set_false_to_retain --remove_digit set_false_to_retain --remove_emoticon set_false_to_retain --remove_stopwords set_false_to_retain
```
It creates a ```path_to_output_file.txt``` file which contains preprocessed text

Note: The aforementioned flags are optional. For more information, run ```preprocess_text.py --help``` or simply ```python preprocess_text.py -h```.
