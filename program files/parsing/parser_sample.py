
from __future__ import unicode_literals, print_function
from pypeg2 import *
from decimal import Decimal

# RegEx for ints and floats
integer = re.compile(r"\d+")
decimal = re.compile(r"[\-\+]?[0-9]*(\.[0-9]+)?")

# PyPEG Classes for the pieces of the Rule 
class integerNumber(int):
	grammar = integer
class decimalNumber(float):
	grammar = decimal

# Rule pieces in order of how the rule is broken down
class RuleType(Keyword):
	grammar = Enum(K("valueRule"), K("typeRule"))

#Right now you have to put a comma after EVERY type, including the last one
class Type(str):
	grammar = word, ","

class TypeList(List):
	grammar = "[", some(Type), "]"

class Relation(Keyword):
	grammar = Enum(K("each"), K("together"))

class Operator(Keyword):
	grammar = Enum(K("greater_than"), K("exactly_to"), K("less_than"))

# Types of Rules 
class valueRule(str):
	#name(), blank, "=", blank, 
	grammar = RuleType, blank, "Categories ", blank, \
				TypeList, blank, Relation, blank, "must sum to", blank, \
				Operator, blank, decimalNumber, "."

class typeRule(str):
	#name(), blank, "=", blank, 
	grammar = RuleType, blank, "Categories ", blank, \
				TypeList, blank, Relation, blank, "must have", blank, \
				Operator, blank, integerNumber, blank, "inputs."

# Most generic form of the rule 
class genericRule(str):
	grammar = name(), blank, "=", blank, [typeRule, valueRule]

