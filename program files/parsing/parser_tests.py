from parser_sample import *
import unittest


class TestParser(unittest.TestCase):
    # Nothing special to set up, pass
    def setUp(self):
        pass 
    # Basic example of word parsing, testing functionality of package
    def test_basic(self):
        exampleWordParse = parse("hello world", some(word))
        self.assertEqual(['hello', 'world'], exampleWordParse)

    # Tests for each component of the rules 
    def test_RuleType(self):
        exampleRuleType = parse ("valueRule", RuleType)
        self.assertEqual(RuleType('valueRule'), exampleRuleType)

        exampleRuleType2 = parse ("typeRule", RuleType)
        self.assertEqual(RuleType('typeRule'), exampleRuleType2)

        # should fail for undefined rule types
        with self.assertRaises(SyntaxError):
            parse("undefinedRule", RuleType)

    def test_Type(self):
        exampleType = parse("a,", Type)
        self.assertEqual("a", exampleType)

        # Right now, enforces comma after each element
        with self.assertRaises(SyntaxError):
            parse("a", Type)
    
    def test_TypeList(self):
        exampleTypeList = parse("[a, b, c,]", TypeList)
        self.assertEqual(TypeList(['a', 'b', 'c']), exampleTypeList)

        # Again, should fail if Type fails 
        with self.assertRaises(SyntaxError):
            parse("[a, b, c]", TypeList)

    def test_Relation(self):
        exampleRelaiton = parse("each", Relation)
        self.assertEqual(Relation("each"), exampleRelaiton)
        #check to make sure enumeration is distinguished from others 
        self.assertNotEqual(Relation("together"), exampleRelaiton)

    def test_Operator(self):
        exampleOperator = parse("exactly_to", Operator)
        self.assertEqual(Operator("exactly_to"), exampleOperator)
        self.assertNotEqual(Operator("less_than"), exampleOperator)
        self.assertNotEqual(Operator("greater_than"), exampleOperator)

    def test_Rules(self):
        # Each type of rule has a test for the rule components and the name
        exampleValueRule = parse("value_rule =  valueRule Categories [a, b, c,] each must sum to greater_than 5.0.", genericRule)
        self.assertEqual("[RuleType(u'valueRule'), TypeList([u'a', u'b', u'c']), Relation(u'each'), Operator(u'greater_than'), 5.0]", exampleValueRule)
        self.assertEqual(Symbol(u'value_rule'), exampleValueRule.name)

        exampleTypeRule = parse ("type_rule = typeRule Categories [a,] together must have less_than 6 inputs.", genericRule)
        self.assertEqual("[RuleType(u'typeRule'), TypeList([u'a']), Relation(u'together'), Operator(u'less_than'), 6]", exampleTypeRule)
        self.assertEqual(Symbol(u'type_rule'), exampleTypeRule.name)

        # cannot parse cross rules 
        with self.assertRaises(SyntaxError):
            parse ("type_rule = typeRule Categories [a,] together must have less_than 6 inputs.", valueRule)

        # Type rules may NOT have a float total
        with self.assertRaises(SyntaxError):
            parse ("type_rule = typeRule Categories [a,] together must have less_than 4.6 inputs.", genericRule)

        with self.assertRaises(SyntaxError):
            parse ("type_rule = typeRule Categories [a,] together must sum to less_than 7 inputs.", genericRule)
        
        # TypeList cannot be empty 
        with self.assertRaises(SyntaxError):
            parse("value_rule =  valueRule Categories [] each must sum to greater_than 5.0.", genericRule)


# automatically run test case when file is invoekd 
if __name__ == '__main__':
    unittest.main()
