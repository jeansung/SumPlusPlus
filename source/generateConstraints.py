#imports
from rule_parser import *
from reference_dictionaries import *
from xlrd import open_workbook
from xlwt import *
from xlutils.copy import copy
import sys
import globals 

# File that takes the rule and table info file to generate the constraints
# and add to the Sandbox file so that it is a usable environment. 

TRUE_MESSAGE = '"good"'
FALSE_MESSSAGE = '"bad"'

RULE_STRING_COL = 0
RULE_NAME_COL = 1
RULE_STATUS = 2
CURRENT_VALUE = 3
TARGET_VALUE = 4



def writeRulesToExcel(ws, nameFormulaPairs, ruleStrings):
	#find space to write it
	ruleStringCol = 0
	nameCol = 1
	formulaCol = 2
	startRow = globals.freeRow + 1

	#  write titles
	ws.write(startRow, RULE_STRING_COL, "Rule")
	ws.write(startRow, RULE_NAME_COL, "Name of the Rule")
	ws.write(startRow, RULE_STATUS, "Rule met?")

	startRow = startRow + 1

	for row in range(len(nameFormulaPairs)):
		adjustedRow = startRow + row
		currRule = ruleStrings[row]
		currName = nameFormulaPairs[row][0]
		currFormula = nameFormulaPairs[row][1]
		ws.write(adjustedRow, ruleStringCol, currRule)
		ws.write(adjustedRow, nameCol, currName)
		ws.write(adjustedRow, formulaCol, Formula(currFormula))

	globals.freeRow = startRow + len(nameFormulaPairs) + 1 
	return 

# Returns a list of tuples (name, formula string) for a list of 
# parsed rules. Using the TYPE_INDEX position to determine which
# rule type (and thus which function) to use in creating Excel
# formula. 
def generateExcelFormulas(parsedRules):
	nameFormula = []
	for r in parsedRules:
		ruleType = r.rule_type.typing 
		if (ruleType == RuleType('valueRule')):
			(name, formula) = createValueRule(r)
			nameFormula.append((name, formula))
		elif (ruleType == RuleType('typeRule')):
			(name, formula) = createTypeRule(r)
			nameFormula.append((name, formula))
		else:
			print "Error. Non supported rule type."
			sys.exit(0)
	return nameFormula

# Creating a typeRule
# Input: Parsed Type Rule
# Output: (Name, Excel formula string)
def createTypeRule(r):
	logicalTest = ""
	operatorStr = OPERATOR_MAPPING[r.rule_type.operator]
	valueStr = str(r.rule_type.value)
	inputColLetter =  EXCEL_ROW_MAPPING[globals.numInputsCol]

	# Parsing Types  => Excel 
	types = r.rule_type.type_list
	sumElements = []
	currentValue = ""
	for t in types:
		row = globals.typeRowMapping[t]
		element = str(inputColLetter) + str(row)
		sumElements.append(element)

	if (r.rule_type.relation == Relation("together")):
		# Creating Sum String 
		innerSum = "+".join(sumElements)
		currentValue = "SUM(" + innerSum + ")"
		logicalTest = currentValue + operatorStr + valueStr 
	elif (r.rule_type.relation == Relation("each")):
		individualCheck = []
		for e in sumElements:
			currentCheck = "(" + str(e) + operatorStr + valueStr + ")"
			individualCheck.append(currentCheck)
		logicalTest = "*".join(individualCheck)
	else:
		print "Error on the relation"
		sys.exit(0)

	formulaStr = "IF(" + logicalTest + "," + TRUE_MESSAGE + "," + \
		FALSE_MESSSAGE + ")"

	# Need to return 
	# name, formula, currentValue, target 
	return (r.name, formulaStr)

# Creating a valueRule
# Input: Parsed Value Rule
# Output: (Name, Excel formula string)
def createValueRule(r):
	logicalTest = ""
	operatorStr = OPERATOR_MAPPING[r.rule_type.operator]
	valueStr = str(r.rule_type.value)
	types = r.rule_type.type_list

	if (r.rule_type.relation == Relation("together")):
		allSumElements = []
		for t in types:
			sumElements = []
			for vLocation in globals.valueColMappingReverse:
				elementColLetter = EXCEL_ROW_MAPPING[vLocation]
				elementRow = globals.typeRowMapping[t]
				element = elementColLetter + str(elementRow)
				weight = str(globals.valueColMappingReverse[vLocation])
				innerSum = "(" + element + "*" + weight + ")"
				sumElements.append(innerSum)
			perTypeWeightedSum = "(" + "+".join(sumElements) + ")"
			allSumElements.append(perTypeWeightedSum)
		totalSumString = "(" + "+".join(allSumElements) + ")"
		logicalTest = "SUM(" + totalSumString + ")" + operatorStr + valueStr 
	elif (r.rule_type.relation == Relation("each")):
		individualCheck = []
		for t in types:
			sumElements = []
			for vLocation in globals.valueColMappingReverse:
				elementColLetter = EXCEL_ROW_MAPPING[vLocation]
				elementRow = globals.typeRowMapping[t]
				element = elementColLetter + str(elementRow)
				weight = str(globals.valueColMappingReverse[vLocation])
				innerSum = "(" + element + "*" + weight + ")"
				sumElements.append(innerSum)
			perTypeWeightedSum = "(" + "+".join(sumElements) + ")"
			currentCheck = "(" + perTypeWeightedSum + operatorStr + \
				valueStr + ")"
			individualCheck.append(currentCheck)
		logicalTest = "*".join(individualCheck)
	else:
		print "Error on the relation"
		sys.exit(0)

	formulaStr = "IF(" + logicalTest + "," + TRUE_MESSAGE + "," + \
		FALSE_MESSSAGE + ")"
	return (r.name, formulaStr)
