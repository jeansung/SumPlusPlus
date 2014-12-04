from TwoWayDict import *
excelCol= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

excelColDictionary = {}
#TwoWayDict()
counter = 0
for index in range(len(excelCol)):
	currentLetter = excelCol[index]
	excelColDictionary[currentLetter] = counter
	counter +=1 

for letter in range(len(excelCol)):
	for letter2 in range(len(excelCol)):
		outerLetter = excelCol[letter]
		innerLetter = excelCol[letter2]
		wholeLetter = outerLetter + innerLetter
		excelColDictionary[wholeLetter] = counter
		counter +=1

print excelColDictionary


