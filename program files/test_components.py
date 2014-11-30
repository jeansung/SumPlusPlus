from rule_parser import *
import unittest


class TestParser(unittest.TestCase):
    # Basic example of word parsing, testing functionality of package
    def test_basicWord(self):
        exampleWordParse = parse("hello world", some(word))
        self.assertEqual(['hello', 'world'], exampleWordParse)
        print exampleWordParse

    # Tests for each component of the rules 
    def test_RuleName(self):
        exampleRuleName = parse("a_sample_name", RuleName)
        self.assertEqual(RuleName("a_sample_name"), exampleRuleName)
        print exampleRuleName

    def test_RuleType(self):
        exampleRuleType = parse ("valueRule", RuleType)
        self.assertEqual(RuleType('valueRule'), exampleRuleType)
        print exampleRuleType

        exampleRuleType2 = parse ("typeRule", RuleType)
        self.assertEqual(RuleType('typeRule'), exampleRuleType2)
        print exampleRuleType2

        # should fail for undefined rule types
        with self.assertRaises(SyntaxError):
            parse("undefinedRule", RuleType)

    def test_Type(self):
        exampleType = parse("a,", Type)
        self.assertEqual("a", exampleType)
        print exampleType

        # Right now, enforces comma after each element
        with self.assertRaises(SyntaxError):
            parse("a", Type)
    
    def test_TypeList(self):
        exampleTypeList = parse("[a, b, c,]", TypeList)
        self.assertEqual(TypeList(['a', 'b', 'c']), exampleTypeList)
        print exampleTypeList

        # Again, should fail if Type fails 
        with self.assertRaises(SyntaxError):
            parse("[a, b, c]", TypeList)

    def test_Relation(self):
        exampleRelation = parse("each", Relation)
        self.assertEqual(Relation("each"), exampleRelation)
        print exampleRelation

        #check to make sure enumeration is distinguished from others 
        self.assertNotEqual(Relation("together"), exampleRelation)

    def test_Operator(self):
        exampleOperator = parse("exactly_to", Operator)
        self.assertEqual(Operator("exactly_to"), exampleOperator)
        self.assertNotEqual(Operator("less_than"), exampleOperator)
        self.assertNotEqual(Operator("greater_than"), exampleOperator)
        print exampleOperator

# automatically run test case when file is invoked 
if __name__ == '__main__':
    unittest.main()
