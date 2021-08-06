! /bin/bash
cd ../fastText
IFS=' '
test_file=''
header_first=''
header_second=''
i=0
pred=1
k=1
for arg in $@
do
	if [ $i -eq 0 ]
	then
		test_file=${arg}
	
	elif [ $i -eq 1 ]
	then
		k=${arg}	
	
	elif [ $i -eq 2 ]
	then
		header_first=${arg}	

	elif [ $i -eq 3 ]
	then
		header_second=${arg}

	else
		echo "Testing ${arg}"
		./fasttext predict-prob ${arg} ${test_file} ${k} > "../predictions_${pred}.txt"
	fi
	i=$((i+1))
	pred=$((pred+1))
done

cd ..
rm predictions.txt
rm predictions.csv
python ensemble.py
python create_predictions.py ${header_first} ${header_second} ${pred}
rm predictions.txt