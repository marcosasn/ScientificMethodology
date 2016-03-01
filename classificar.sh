#!/bin/bash  
        
tecnica=$1
datapathtreino=$2
datapathteste=$3
output=$4

> data_treino.arff
echo "@RELATION data" >> data_treino.arff
echo "@ATTRIBUTE tem_link {True, False}" >> data_treino.arff
echo "@ATTRIBUTE tamanho NUMERIC" >> data_treino.arff
echo "@DATA" >> data_treino.arff
pasta=$datapathtreino
for f in $(ls $pasta);
do
	python extrator_caracteristicas.py $f $datapathtreino data_treino.arff
done;

> data_teste.arff
echo "@RELATION data" >> data_teste.arff
echo "@ATTRIBUTE tem_link {True, False}" >> data_teste.arff
echo "@ATTRIBUTE tamanho NUMERIC" >> data_teste.arff
echo "@DATA" >> data_teste.arff
pasta=$datapathteste
for f in $(ls $pasta);
do
	python extrator_caracteristicas.py $f $datapathteste data_teste.arff
done;

cls.py tecnic data_treino.arff data_teste.arff
echo $tecnica

