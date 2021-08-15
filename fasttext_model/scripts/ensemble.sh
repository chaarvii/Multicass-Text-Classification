#! /bin/bash
rm ../predictions.txt
rm ../predictions.csv
cd ../fastText
test_file=''
header_first=''
header_second=''
i=0
pred=0
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
		pred=$((pred+1))
		./fasttext predict-prob ${arg} ${test_file} ${k} > "../predictions_${pred}.txt"
	fi
	i=$((i+1))
done

cd ..
python ensemble.py --models ${pred}
python create_predictions.py --header_first ${header_first} --header_second ${header_second}