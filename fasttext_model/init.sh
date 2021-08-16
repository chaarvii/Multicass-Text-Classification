#! /bin/bash

chmod +x ./scripts/build_fasttext.sh
chmod +x ./scripts/train.sh
chmod +x ./scripts/infer.sh
chmod +x ./scripts/ensemble.sh
cd scripts
./build_fasttext.sh
python -m spacy download en_core_web_sm
mkdir ../models
mkdir ../dataset
mkdir ../results