import sys 
import codecs
import os.path
from rule_parser import *

# Messages 
GET_INT_OPTION = "Please enter: \n[0] for table creation \n[1] for rule generation \
			 \n[-1] for quit. \n"
TRY_AGAIN_MESSAGE = "Try again. Not a valid supported option"
GOODBYE_MESSAGE = "Okay, goodbye."
GET_TABLE_FILE = "Table file name (txt file) or Q for quit: "
GET_RULE_FILE = "Rule file name (txt file) or Q for quit: "
GET_OUTPUT_FILENAME = "Output File Name or Q for quit: "

# Default input location
INPUT_LOCATION = "/../input_files/"

# Public Methods 
def processInitialOptions():
	while True:
		try:
			intOption = int(raw_input(GET_INT_OPTION))
			break
		except ValueError:
			print TRY_AGAIN_MESSAGE

	if (intOption == -1):
		print GOODBYE_MESSAGE
		sys.exit(0)

	return intOption

def isRuleCreate(intOption):
	return intOption == 1


def collectTable():

	while True:
		try:
			tablefileName = raw_input(GET_TABLE_FILE)
			if (tablefileName == "Q"):
				sys.exit(0)
			tableFile = codecs.open(os.path.dirname(__file__) + \
				INPUT_LOCATION + tablefileName)
			break
		except IOError:
			print "Table file incorrectly formatting or does not exist."

	types = tableFile.readline().rstrip().split(",")
	values = tableFile.readline().rstrip().split(",")
	values = checkValues(values)

	tableFile.close()

	return (types, values)


def collectRules():	
	ruleStrings = []

	while True:
		try:
			ruleFileName = raw_input(GET_RULE_FILE)
			if (ruleFileName == "Q"):
				sys.exit(0)
			ruleFile = codecs.open(os.path.dirname(__file__) + INPUT_LOCATION \
				+ ruleFileName)
			break
		except IOError:
			print "Rule file incorrectly formatting or does not exist."
	for l in ruleFile:
		l = l.rstrip()
		ruleStrings.append(l)
	ruleFile.close()
	return ruleStrings

def collectExcelFileName():
	outputFileName = raw_input(GET_OUTPUT_FILENAME)
	if (outputFileName == "Q"):
		sys.exit(0)
	return outputFileName

	
def checkValues(values):
	valuesNum = []
	for v in values:
		try:
			v = float(v)
			valuesNum.append(v)
		except ValueError:
			print "Badly formed input values."
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
			print "Incorrectly formatted rule. See parser for more."
			sys.exit(0)
	return rules 
	