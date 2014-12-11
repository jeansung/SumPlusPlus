import sys 
import codecs
import os.path
from rule_parser import *

# Messages 
GET_INT_OPTION = "Please enter: \n \
	 [0] for Table Creation \n \
	 [1] for Rule Generation \n \
 	 [2] for Sample Program 1: Table Creation \n \
 	 [3] for Sample Program 2: Rule Generation \n \
 	 [-1] for Quit. \n\n"

TRY_AGAIN_MESSAGE = "Try again. Not a valid supported option"
GOODBYE_MESSAGE = "Okay, goodbye."
GET_TABLE_FILE = "Table file name (txt file) or Q for quit: "
GET_RULE_FILE = "Rule file name (txt file) or Q for quit: "
GET_OUTPUT_FILENAME = "Output File Name or Q for quit: "
QUIT_OPTION = "Q"

# Error messages
TABLE_FILE_IO_ERROR_MSG = "Table file incorrectly formatting or does not exist."
RULE_FILE_IO_ERROR_MSG = "Rule file incorrectly formatting or does not exist."
VALUE_FORMAT_ERROR_MSG = "Error: Values in the table must be numbers (integers \
of decimals)."
BAD_RULE_PARSE_ERROR_MSG = "Incorrectly formatted rule. See parser/grammar for \
 more."

# Labels 
SP1_INT = 2
SP2_INT = 3
SP1_STRING = "sampleprogram1"
SP2_STRING = "sampleprogram2"

# Default input location
INPUT_LOCATION = "/../input_files/"

# Max supported int option
MAX_INT_OPTION = 3


# Public Methods 

# Method to process the options of the user 
def processInitialOptions():
	while True:
		try:
			intOption = int(raw_input(GET_INT_OPTION))
			break
		except ValueError or (intOption > MAX_INT_OPTION):
			print TRY_AGAIN_MESSAGE

	if (intOption == -1):
		print GOODBYE_MESSAGE
		sys.exit(0)

	return intOption

# boolean setters 
def isRuleCreate(intOption):
	return intOption == 1

def isSampleProgram(intOption):
	return intOption > 1
# sets sample number
def whichSample(intOption):
	if (intOption == SP1_INT):
		return SP1_STRING
	elif (intOption == SP2_INT):
		return SP2_STRING
	else:
		return

# Collecting the table file
def collectTable():
	while True:
		try:
			tablefileName = raw_input(GET_TABLE_FILE)
			if (tablefileName == QUIT_OPTION):
				sys.exit(0)
			tableFile = codecs.open(os.path.dirname(__file__) + \
				INPUT_LOCATION + tablefileName)
			break
		except IOError:
			print TABLE_FILE_IO_ERROR_MSG 
	bareTypes = "".join(tableFile.readline().split())
	types = bareTypes.split(",")
	bareValues = "".join(tableFile.readline().split())
	values = bareValues.split(",")
	values = checkValues(values)

	tableFile.close()
	return (types, values)


# Collect the rule file
def collectRules():	
	ruleStrings = []
	while True:
		try:
			ruleFileName = raw_input(GET_RULE_FILE)
			if (ruleFileName == QUIT_OPTION):
				sys.exit(0)
			ruleFile = codecs.open(os.path.dirname(__file__) + INPUT_LOCATION \
				+ ruleFileName)
			break
		except IOError:
			print RULE_FILE_IO_ERROR_MSG 

	for l in ruleFile:
		l = l.rstrip()
		ruleStrings.append(l)

	ruleFile.close()
	return ruleStrings

# Collecting the Excel file name 
def collectExcelFileName():
	outputFileName = raw_input(GET_OUTPUT_FILENAME)
	if (outputFileName == QUIT_OPTION):
		sys.exit(0)
	return outputFileName

# Private helper methods

# Checks that the values are well formed, that they are ints or floats.
def checkValues(values):
	valuesNum = []
	for v in values:
		try:
			v = float(v)
			valuesNum.append(v)
		except ValueError:
			print VALUE_FORMAT_ERROR_MSG 
			sys.exit(0)

	return valuesNum

# Returns a list of parsed rules (a list of genericRule Objects)
def parseRules(ruleStringList):
	rules = []
	for rule in ruleStringList:
		try:
			currentRule = parse(rule, genericRule)
			rules.append(currentRule)
		except SyntaxError:
			print BAD_RULE_PARSE_ERROR_MSG
			sys.exit(0)
	return rules 
	