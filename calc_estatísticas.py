# encoding: utf-8
import sys

name_actual = sys.argv[1]
name_predicted = sys.argv[2]
f = open(name_actual)
get_coluna = lambda f : map(lambda actual : int(actual[0]), filter(lambda actual : len(actual) > 0 and actual[0].isdigit(), map(lambda actual : actual.split(), f.read().split('\n'))))
get_coluna2 = lambda f : map(lambda actual : int(actual[0]), filter(lambda actual : len(actual) > 1 and actual[0].isdigit(), map(lambda actual : actual.split(), f.read().split('\n'))))
actual = get_coluna(f)
f.close()
f = open(name_predicted)
predicted = get_coluna2(f)
f.close()
values = list(set(actual + predicted))
matrix = []
for i in range(len(values)):
	matrix.append([])
	for j in range(len(values)):
		matrix[-1].append(0)
for a, p in zip(actual, predicted):
	matrix[a - 1][p - 1] += 1

tp = matrix[0][0]
fn = matrix[0][1]
fp = matrix[1][0]
tn = matrix[1][1]
precision = tp / float(tp + fp)
recall = tp / float(tp + fn)
fmeasure = (2*precision*recall)/float(precision + recall)
out = open("out.txt", "w")
out.write("precision: " + str(precision) +"\n")
out.write("recall: " + str(recall) + "\n")
out.write("f-measure: " + str(fmeasure) + "\n")
out.close()
#print "precision: " + str(precision)
#print "recall: " + str(recall)
#print "f-measure: " + str(fmeasure)
#return (precision,recall,fmeasure)
