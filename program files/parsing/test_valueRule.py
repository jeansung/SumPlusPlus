from rule_parser import *
import unittest


class TestParser(unittest.TestCase):
    def test_SimpleValueRule(self):
        exampleValueRule = parse ("v2 = valueRule Categories [a, b, c,]\
         each must sum to exactly_to 9.5.", genericRule)
        self.assertEqual(genericRule([], name=u'v2'), exampleValueRule)
        print exampleValueRule

        # checking the components of the rule 
        self.assertEqual("v2", exampleValueRule.name)
        print "name: ", exampleValueRule.name
        self.assertEqual(RuleType(u'valueRule'), \
            exampleValueRule.rule_type.typing)
        print "type: ", exampleValueRule.rule_type.typing
        self.assertEqual(TypeList(['a', 'b', 'c',]), \
            exampleValueRule.rule_type.type_list)
        print"type list: ", exampleValueRule.rule_type.type_list
        self.assertEqual(Relation("each"), \
            exampleValueRule.rule_type.relation)
        print "relation: ", exampleValueRule.rule_type.relation
        self.assertEqual(Operator("exactly_to"), \
            exampleValueRule.rule_type.operator)
        print "operator: ", exampleValueRule.rule_type.operator
        self.assertEqual(9.5, exampleValueRule.rule_type.value)
        print "value: ", exampleValueRule.rule_type.value

        

    def test_SeveralTypeRules(self):
        rule1 = parse ("r1 = typeRule Categories [a, b, c, e,] together \
         must have less_than 7 inputs.", genericRule)
        rule2 = parse ("r2 = typeRule Categories [a, b,] together \
         must have less_than 8 inputs.", genericRule)
        pass


# automatically run test case when file is invoked 
if __name__ == '__main__':
    unittest.main()
