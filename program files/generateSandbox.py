import xlwt
import codecs
import sys
from excelMapping import EXCEL_ROW_MAPPING 
from utilityIO import *

## Currently:
# - must run program with 2 input files and a name for your output excel file
# - assumes table and rules are well formed

# TODO:
# - run program with zero inputs, while true loop to collect file names
# and output excel name
# - instead of free row and column, find a better way to specific free/ occupied
# 	- hash table? (check before inserting, hash after)
# 	- need to add support for Labels

# Different Files 
# File IO Functions with error checking for correctness
# that have functions to return table and rules
# Parse Rules
#  
# Creating the initial table on Excel table 

# formulaString
# worksheet: ws
# ws.write(2, 2, xlwt.Formula(formulaString))


EXCEL_FILE_EXTENSION = ".xls"
TABLE_BUFFER_ROW = 1
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
	(freeRow, freeCol, types, values) = createInitialTable(wb, ws, typeFileName,
		 valueFileName,
		 freeRow, freeCol)

	# calculate input sums/ # inputs per table 
	(freeRow, freeCol, intermediateSumRow) = createSumFromDifficulty(wb, ws,
		 types, values, freeRow, freeCol)
	(freeRow, freeCol, numInputsColumn) = createNumberOfInputs(wb, ws, types,
		 values, freeRow, freeCol)


	# input rules 
	# Parse rules under the assumption that they 
	# Hardcoded for now, will implement as taking in stuff later 
	rule1 = limitTotalSum(">", 10, values, intermediateSumRow+1 )
	ws.write(freeRow+5, 3, xlwt.Formula(rule1))


	wb.save(outputFileName + EXCEL_FILE_EXTENSION)

	return 


## Rule Creation Methods (to change after grammar)
## Return Strings right now
# =IF(SUM(B6:D6)>10,0,1)
# If the total sum is greater than 10, "GOOD" otherwise bad 
def limitTotalSum(operator, totalValue, values, intermediateSumRow):
	rowStart = 1
	rowStartStr = EXCEL_ROW_MAPPING[rowStart] + str(intermediateSumRow)
	rowEnd = rowStart + len(values) -1
	rowEndStr = EXCEL_ROW_MAPPING[rowEnd] + str(intermediateSumRow)


	innerFormulaStr = "SUM(" + rowStartStr + ":" + rowEndStr + ")"
	formulaStr = "IF(" + innerFormulaStr + operator + str(totalValue) \
		 + "," + "0" + "," + "1" + ")"
	return formulaStr

#def limitTotalInputs(operator, totalNumber, types, numInputsColumn):


## Helper methods 

# Check to see if command line arguments are correct 
def properInputFiles():
	try:
		typeFileName = sys.argv[1]
		valueFileName = sys.argv[2]
		outputFileName = sys.argv[3]
		return (typeFileName, valueFileName, outputFileName)
	except IndexError or TypeError:
		print "Incorrect run of program. Must run as python2 generateSandbox.py \
		 types.txt values.txt outputFileName"
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
		numInputsColumn = endColIndex + TABLE_BUFFER_ROW
		# write it in the row col
		ws.write(row, col, xlwt.Formula(formulaStr))

	freeCol = freeCol + TABLE_BUFFER_COL + 1
	return (freeRow, freeCol, numInputsColumn)

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

		formulaStr = "SUM(" + startRowStr + ":" + endRowStr  + ")" + "*"  \
			+ multiplierRowStr

		row = freeRow + TABLE_BUFFER_ROW
		col = adjIndex

		ws.write(row, col, xlwt.Formula(formulaStr))

	intermediateSumRow = freeRow + TABLE_BUFFER_ROW
	freeRow = freeRow + TABLE_BUFFER_ROW + 1 
	return (freeRow, freeCol, intermediateSumRow )	


# automatically runs main method when script runs
if __name__ == "__main__":main()
