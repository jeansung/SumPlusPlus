excelCol= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

excelColDictionary = {}
for index in range(len(excelCol)):
	currentLetter = excelCol[index]
	excelColDictionary[currentLetter] = index

print excelColDictionary