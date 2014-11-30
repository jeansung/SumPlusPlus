# Helper method for generateSandbox.py
# Given information, writes to text file

FILE_NAME_SUPPORT = "SUPPORT"
FILE_EXTENSION = ".txt"
TITLE = "This is a support file for the Excel Sandbox file generated. DO NOT MO\
DIFY!! \n\n"

def createExcelInfo(outputFileName, freeRow, freeCol, numInputsCol, \
	intermediateSumRow, typeRowMappingDictionary, valueColMappingDictionary):
	outputContents = [outputFileName, str(freeRow), str(freeCol), \
		str(numInputsCol), str(intermediateSumRow), \
		str(typeRowMappingDictionary), str(valueColMappingDictionary)]
	infoString = TITLE + "\n".join(outputContents)

	return infoString

def writeToFile(infoString, excelFileName):
	try:
		outputFile = open(str(excelFileName)+FILE_NAME_SUPPORT+FILE_EXTENSION, "w")
		outputFile.write(infoString)
		outputFile.close()
	except IOError:
		print "Error in creating supporting file."
		sys.exit(0)