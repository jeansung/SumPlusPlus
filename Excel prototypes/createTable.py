import xlwt
import codecs
import sys

from datetime import datetime

# you must program with 2 input fillesand a name for your output excel file
# eventually change so that you run with nothing and force while loop to take
#in  the 3 inputs
# LIMITATIONS:
# -  Only supports excel file through 26 values (Need to feed it more of the excel columns)
# Maximum excel coulm XFD 
# Formula: 	# ws.write(2, 2, xlwt.Formula("A3+B3"))

EXCEL_ROW_MAPPING = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

EXCEL_FILE_EXTENSION = ".xls"
TABLE_BUFFER_ROW = 2
TABLE_BUFFER_COL = 2

def main():
	# check inputs 
	(typeFileName, valueFileName, outputFileName) = properInputFiles()

	# variables to keep track of where I can put things next 
	freeRow = 0
	freeCol = 0

	# create workbook and worksheet
	wb = createWorkbook()
	ws = createWorksheet(wb, "abcdefghijklmnop")

	# parse initial table
	(freeRow, freeCol, types, values) = createInitialTable(wb, ws, typeFileName, valueFileName,
		 freeRow, freeCol)

	# calculate input sums/ # inputs per table 
	(freeRow, freeCol) = createSumFromDifficulty(wb, ws, types, values, freeRow, freeCol)
	(freeRow, freeCol) = createNumberOfInputs(wb, ws, types, values, freeRow, freeCol)

	# input rules 
	# Parse rules under the assumption that they 
	# are correct (refer to table included )


	print freeRow
	print freeCol
	wb.save(outputFileName + EXCEL_FILE_EXTENSION)

	return 

# Create column that counts number 
def createNumberOfInputs(wb, ws, types, values, freeRow, freeCol):
	for type in range (0, len(types)):
		adjIndex = type + 1
		#Default for now 
		startColIndex = 1
		startCol = EXCEL_ROW_MAPPING[startColIndex]
		endColIndex = startColIndex + len(values) - 1
		endCol = EXCEL_ROW_MAPPING[endColIndex]


		startColStr = str(startCol) + str(adjIndex+1)
		endColStr = str(endCol) + str(adjIndex+1)


		formulaStr  = "SUM(" + startColStr + ":" + endColStr  + ")"

		row = adjIndex
		col = endColIndex + TABLE_BUFFER_ROW
		# write it in the row col
		ws.write(row, col, xlwt.Formula(formulaStr))
	freeCol = freeCol + TABLE_BUFFER_COL + 1
	return (freeRow, freeCol)


	# create # input tables
	# for each of the rows (i.e. types) so through the number of values
	# col start,  get letter 
	# col end , get letter
	# row number is index 
	# Sum (Start: Ennd)





# Create row of sums from each multiplier 
def createSumFromDifficulty(wb, ws, types, values, freeRow, freeCol):
	for difficulty in range(len(values)):
		adjIndex = difficulty + 1

		colLetter = EXCEL_ROW_MAPPING[adjIndex]
		multiplierRow = 1
		startRow = multiplierRow + 1
		endRow = startRow + (len(types) -1)

		multiplierRowStr = colLetter + str(multiplierRow)
		startRowStr = colLetter + str(startRow)
		endRowStr = colLetter + str(endRow)

		formulaStr = "SUM(" + startRowStr + ":" + endRowStr  + ")" + "*" + multiplierRowStr

		row = freeRow
		col = adjIndex

		ws.write(row, col, xlwt.Formula(formulaStr))

	freeRow = freeRow + 1 
	return (freeRow, freeCol)	



# Check to see if command line arguments are correct 
def properInputFiles():
	try:
		typeFileName = sys.argv[1]
		valueFileName = sys.argv[2]
		outputFileName = sys.argv[3]
		return (typeFileName, valueFileName, outputFileName)
	except IndexError or TypeError:
		print "Incorrect run of program. Must run as python2 createTable.py types.txt values.txt outputFileName"
		sys.exit(0) 

def createWorkbook():
	return xlwt.Workbook()

def createWorksheet(workbook, sheetName):
	return workbook.add_sheet(sheetName);

# Create initial types/ values table 
def createInitialTable(wb, ws, typeFileName, valueFileName, freeRow, freeCol):
	types = inputTypes(typeFileName)
	values = inputValues(valueFileName)

	for typeIndex in range(len (types)):
		adjIndex = typeIndex +1
		ws.write(adjIndex, 0, types[typeIndex])
		freeRow = adjIndex + 1

	for valueIndex in range(len (values)):
		adjIndex = valueIndex + 1
		ws.write(0, adjIndex, values[valueIndex])
		freeCol = adjIndex +1 

	return (freeRow, freeCol, types, values) 


# Takes a file name as a string
# Returns a list of strings of types
def inputTypes(filename):
	types = []
	try:
		file = codecs.open(filename)
	except IOError:
		print "Types file incorrectly formatting or does not exist."
		sys.exit(0)

	for line in file:
		line = line.rstrip()
		types.append(line)
	file.close()
	return types

# Takes a file name as a string
# Returns a list of ints for values 
def inputValues(filename):
	values = []
	try:
		file = codecs.open(filename)
	except IOError:
		print "Values file incorrectly formatted or does not exist."
		sys.exit(0)

	for line in file:
		line = line.rstrip()
		try:
			numValue = int(line)
		except ValueError:
			print "Badly formed input values."
			sys.exit(0)
		values.append(numValue)
	file.close()
	return values


# automatically runs main method when script runs
if __name__ == "__main__":main()
