#!/bin/bash  
        
tecnica=$1
datapathtreino=$2
datapathteste=$3

if [[ $tecnica == "svm" ]];
then

pasta=$datapathtreino
for f in $(ls $pasta);
do
    for l in $(ls $pasta'/'$f);
        do
	        python extrator_caracteristicas.py $l $datapathtreino/$f data_treino.libsvm
        done;
done;

pasta=$datapathteste
for f in $(ls $pasta);
do
	for l in $(ls $pasta'/'$f);
		do
			python extrator_caracteristicas.py $l $datapathteste/$f data_teste.libsvm

		done;
done;

cd classifier
./svm-train -b 1 ../data_treino.libsvm > test.txt
./svm-predict -b 1 ../data_teste.libsvm data_treino.libsvm.model output.txt > test.txt
rm  test.txt
cd ..
python calc_estatísticas.py data_teste.libsvm classifier/output.txt 
cat out.txt
rm out.txt

else
	>&2 echo "Técnica inválida"
fi




