import sys
import codecs
from rule_parser import *

def properInputFiles():
	try:
		ruleFileName = sys.argv[1]
		supportingFileName = sys.argv[2]
		return (ruleFileName, supportingFileName)
	except IndexError or TypeError:
		print "Incorrect run of program. Must run as python \
		generateConstraints.py rules.txt supportingFileName.txt"
		sys.exit(0) 

# Returns a list of string rules
def readRulesFromInputFile(filename):
	ruleStrings = []
	try:
		file = codecs.open(filename)
	except IOError:
		print "Rules file incorrectly formatted or does not exist."
		sys.exit(0)
	for l in file:
		l = l.rstrip()
		ruleStrings.append(l)
	file.close()
	return ruleStrings

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
