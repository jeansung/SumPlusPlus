excelCol= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

excelColDictionary = {}
counter = 0
for index in range(len(excelCol)):
	currentLetter = excelCol[index]
	excelColDictionary[counter] = currentLetter
	counter +=1 

for letter in range(len(excelCol)):
	for letter2 in range(len(excelCol)):
		outerLetter = excelCol[letter]
		innerLetter = excelCol[letter2]
		excelColDictionary[counter] = outerLetter + innerLetter
		counter +=1


