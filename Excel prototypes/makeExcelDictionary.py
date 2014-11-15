excelCol= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

excelColDictionary = {}
for index in range(len(excelCol)):
	currentLetter = excelCol[index]
	excelColDictionary[index] = currentLetter

print excelColDictionary