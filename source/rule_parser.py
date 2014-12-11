# imports 
from __future__ import unicode_literals, print_function
from pypeg2 import *
from decimal import Decimal

# Final Grammar 
'''
// primitive things 
letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" ;
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
decimal_point = "." ;
decimal_value = { digit }, decimal_point, { digit } ;

// name is an identifier for a rule
name = { letter } ;

// Total inputs must be an int
// Total of the value may be a double
totalInputs = { digit } ;
totalValues = { decimal_value } ;

// A type is any word (i.e. made up of letters)
type = { letter }; 
types = { type }

// Other rule parts
operator = less_than | exactly_to | greater_than ;
relation = "each" | "together" ;

// Rule types 
typeRule =  Categories (types) (relation) must have (operator) \
		    (totalInputs) inputs. ;
valueRule = Categories (types) (relation) must sum to (operator) \
			(totalValues). ;
genericRule = typeRule | valueRule ;
Rule = name,  "=", genericRule;
Rules = {Rule} ; 
'''

# Parser 
# RegEx for ints and floats
integer = re.compile(r"\d+")
decimal = re.compile(r"[\-\+]?[0-9]*(\.[0-9]+)?")

# PyPEG Classes for the pieces of the Rule 
class integerNumber(int):
	grammar = integer
class decimalNumber(float):
	grammar = decimal

class RuleName(str):
	grammar = word

# Rule pieces in order of how the rule is broken down
class RuleType(Keyword):
	grammar = Enum(K("valueRule"), K("typeRule"))

class TypeList(List):
	grammar = "[", csl(word), "]"

class Relation(Keyword):
	grammar = Enum(K("each"), K("together"))

class Operator(Keyword):
	grammar = Enum(K("greater_than"), K("exactly_to"), K("less_than"))

class typeRule(List): 
    grammar = attr("typing", RuleType), "Categories", \
    		  attr("type_list", TypeList), attr("relation", Relation), \
    		  "must", "have", attr("operator", Operator), \
    		  attr("value", integerNumber), "inputs", "."

class valueRule(List):
    grammar = attr("typing", RuleType), "Categories", \
    		  attr("type_list", TypeList), attr("relation", Relation), \
    		  "must", "sum", "to", attr("operator", Operator), \
    		  attr("value", decimalNumber), "."

# Most generic form of the rule 
class genericRule(List):
	grammar = attr("name", RuleName), "=", attr("rule_type",\
			  [typeRule, valueRule])

# class Rules(List):
# 	grammar = maybe_some(genericRule, blank)
