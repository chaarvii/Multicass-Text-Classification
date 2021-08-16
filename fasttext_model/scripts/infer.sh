#! /bin/bash
cd ../fastText
echo "Starting Inferencing"
./fasttext predict $1 $2 > ../predictions.txt
echo "Completed Inferencing - check predictions.txt"
cd ..
python create_predictions.py
mv predictions* ../results
echo "Check predictions.csv in results"