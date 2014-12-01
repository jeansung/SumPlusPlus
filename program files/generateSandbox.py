import xlwt
import codecs
import sys
from process_table import *
from write_Excel_info import *
from reference_dictionaries import EXCEL_ROW_MAPPING 

# Global constants
INPUT_COL_TITLE = "# inputs"
INTERMEDIATE_SUM_ROW_TITLE = "col sum"

EXCEL_FILE_EXTENSION = ".xls"
TABLE_BUFFER_ROW = 1
TABLE_BUFFER_COL = 2



# Global Variables
freeRow = 0
freeCol = 0
numInputsCol = 0
intermediateSumRow = 0
types = []
values = []
typeRowMapping = {}
valueColMapping = {}
valueColMappingReverse = {}

def main():
	# read table files
	(tableFileName, outputFileName) = properInputFiles()
	global types
	global values
	types, values = inputTable(tableFileName)

	# create Excel worksheet 
	wb = createWorkbook()
	ws = createWorksheet(wb, "Sheet 1")

	# create initial table
	createInitialTable(ws, types, values)

	# create intermediate table
	global intermediateSumRow
	intermediateSumRow = createIntermediateSumRow(ws,
		 types, values)
	global numInputsCol
	numInputsCol = createNumInputsCol(ws, types,
		 values)

	# write to Excel file
	wb.save(outputFileName + EXCEL_FILE_EXTENSION)

	# write to auxiliary text file

	infoString = createExcelInfo(outputFileName, freeRow, freeCol, \
		numInputsCol, intermediateSumRow, typeRowMapping, valueColMapping, \
		valueColMappingReverse)
	writeToFile(infoString, outputFileName)
	
	return 

## Helper methods 
def createWorkbook():
	return xlwt.Workbook()

def createWorksheet(workbook, sheetName):
	return workbook.add_sheet(sheetName);

# Create initial types/ values table 
def createInitialTable(ws, types, values):
	for typeIndex in range(len (types)):
		adjIndex = typeIndex +1
		currentType = types[typeIndex]
		typeRowMapping[currentType] = adjIndex + 1
		ws.write(adjIndex, 0, currentType)

		global freeRow
		freeRow = adjIndex + 1

	for valueIndex in range(len (values)):
		adjIndex = valueIndex + 1
		currentValue = values[valueIndex]
		valueColMapping[currentValue] = adjIndex
		valueColMappingReverse[adjIndex] = currentValue
		ws.write(0, adjIndex, currentValue)
		global freeCol
		freeCol = adjIndex +1 

	return

# Create column that counts number of inputs
def createNumInputsCol(ws, types, values):

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
		numInputsColumn = endColIndex + TABLE_BUFFER_ROW
		# write it in the row col
		ws.write(row, numInputsColumn, xlwt.Formula(formulaStr))

	# writing the title
	ws.write(0, numInputsColumn, INPUT_COL_TITLE)
	global freeCol
	freeCol = freeCol + TABLE_BUFFER_COL + 1
	return numInputsColumn

# Create row of sums from each multiplier 
def createIntermediateSumRow(ws, types, values):
	global freeRow
	global intermediateSumRow
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

		intermediateSumRow = freeRow + TABLE_BUFFER_ROW
		col = adjIndex

		ws.write(intermediateSumRow, col, xlwt.Formula(formulaStr))

	# writing the title
	ws.write(intermediateSumRow, 0, INTERMEDIATE_SUM_ROW_TITLE)
	freeRow = freeRow + TABLE_BUFFER_ROW + 1 
	return intermediateSumRow


# automatically runs main method when script runs
if __name__ == "__main__":main()
