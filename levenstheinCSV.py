import csv
import Levenshtein as lv



PATH = '20210103_hundenamen.csv'
COMPARE_STRING = 'Luca'
TARGET_DIST = 1

def readCsv(path,separator,numCols):
	with open(path, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=separator)
		#Remove Empty and/or invalid rows
		return [r for r in reader if len(r) == numCols]


def extractRelevantValues(rowList):
	#Remove Header Row and only extract values of first column (names)
	relevantValues = [x[0] for x in rowList[1:]]
	#remove duplicate values
	return set(relevantValues)


if __name__ == "__main__":
	rowList = readCsv(PATH,',',3)
	relevantValues = extractRelevantValues(rowList)
	#Calculate distances of values to target string
	distances = [(x,lv.distance(COMPARE_STRING,x)) for x in relevantValues]
	#filter for relevant candidates
	targetValues = list(filter(lambda x: x[1] == TARGET_DIST,distances))
	print(targetValues)
	#Easy to Copy and Paste List
	print(",".join([x[0] for x in targetValues]))


