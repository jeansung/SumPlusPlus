#imports
from source.commandLine import *
from source.generateSandbox import *
from source.generateConstraints import *
from source.rule_parser import *
from source.reference_dictionaries import *
from source.run_sample import *
from xlrd import open_workbook
from xlwt import *
from xlutils.copy import copy
import codecs
import sys
import os

# Rule variables
ruleStrings = ""
parsedRules = ""

# Default output location
OUTPUT_LOCATION = "/output_files/"
OPEN_COMMAND = "open "
# Excel File extension
EXCEL_FILE_EXTENSION = ".xls"

def main():
	# Get all global variables ready
	globals.init()

	# Process user options
	intOption = processInitialOptions()

	# Create Rule Mode Flag
	isCreateRule = isRuleCreate(intOption)

	# isSample Flag
	isSample = isSampleProgram(intOption) 
		
	# Defer to Sample Run 
	if (isSample):
		sampleType = whichSample(intOption)
		if (sampleType == "sampleprogram1"):
			runSample1()
		elif (sampleType == "sampleprogram2"):
			runSample2()
		return


	# Collect Table
	(types, values) = collectTable()

	# if isCreateRule Collect Rules
	if (isCreateRule):
		global ruleStrings
		ruleStrings = collectRules()

		global parsedRules
		parsedRules = parseRules(ruleStrings)

	# Collect Output Filename
	outputFileName = collectExcelFileName()

	# Create Excel file, initial table  
	wb = createWorkbook()
	ws = createWorksheet(wb, "Sheet 1")
	createInitialTable(ws, types, values)

	# Create intermediate tables 
	createIntermediateSumRow(ws, types, values)
	globals.numInputsCol = createNumInputsCol(ws, types, values)

	# if isCreateRule create Excel formulas, write to file
	if(isCreateRule):
		nameFormulaPairs = generateExcelFormulas(parsedRules)
		writeRulesToExcel(ws, nameFormulaPairs, ruleStrings)

	# Save and Launch
	newFile = OUTPUT_LOCATION + outputFileName + EXCEL_FILE_EXTENSION
	localDir = os.path.dirname(os.path.realpath(__file__)) 
	wb.save(localDir+ newFile)  
	os.system(OPEN_COMMAND + localDir + newFile)
	return


# automatically runs main method when script runs
if __name__ == "__main__":main()