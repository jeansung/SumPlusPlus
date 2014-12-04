import xlwt
import sys
from reference_dictionaries import EXCEL_ROW_MAPPING 
import globals


TABLE_BUFFER_ROW = 1
TABLE_BUFFER_COL = 2
INTERMEDIATE_SUM_ROW_TITLE = "col sum"
INPUT_COL_TITLE = "# inputs"

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
		globals.typeRowMapping[currentType] = adjIndex + 1
		ws.write(adjIndex, 0, currentType)
		globals.freeRow = adjIndex + 1

	for valueIndex in range(len (values)):
		adjIndex = valueIndex + 1
		currentValue = values[valueIndex]
		globals.valueColMapping[currentValue] = adjIndex
		globals.valueColMappingReverse[adjIndex] = currentValue
		ws.write(0, adjIndex, currentValue)
		globals.freeCol = adjIndex +1 
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
		globals.numInputsColumn = endColIndex + TABLE_BUFFER_ROW
		# write it in the row col
		ws.write(row, globals.numInputsColumn, xlwt.Formula(formulaStr))

	# writing the title
	ws.write(0, globals.numInputsColumn, INPUT_COL_TITLE)
	globals.freeCol = globals.freeCol + TABLE_BUFFER_COL + 1
	return globals.numInputsColumn

# Create row of sums from each multiplier 
def createIntermediateSumRow(ws, types, values):
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

		globals.intermediateSumRow = globals.freeRow + TABLE_BUFFER_ROW
		col = adjIndex

		ws.write(globals.intermediateSumRow, col, xlwt.Formula(formulaStr))

	# writing the title
	ws.write(globals.intermediateSumRow, 0, INTERMEDIATE_SUM_ROW_TITLE)
	globals.freeRow = globals.freeRow + TABLE_BUFFER_ROW + 1 
	return 
