from rule_parser import *
import unittest


class TestParser(unittest.TestCase):

    def test_SimpleTypeRule(self):
        exampleTypeRule = parse ("type_rule = typeRule Categories [a,] \
            together must have less_than 6 inputs.", genericRule)
        self.assertEqual(genericRule([], name=u'type_rule'), exampleTypeRule)
        print exampleTypeRule

        # checking the components of the rule 
        self.assertEqual("type_rule", exampleTypeRule.name)
        print "name: ", exampleTypeRule.name
        self.assertEqual(RuleType(u'typeRule'), \
            exampleTypeRule.rule_type.typing)
        print "type: ", exampleTypeRule.rule_type.typing
        self.assertEqual(TypeList([u'a',]), \
            exampleTypeRule.rule_type.type_list)
        print"type list: ", exampleTypeRule.rule_type.type_list
        self.assertEqual(Relation("together"), \
            exampleTypeRule.rule_type.relation)
        print "relation: ", exampleTypeRule.rule_type.relation
        self.assertEqual(Operator("less_than"), \
            exampleTypeRule.rule_type.operator)
        print "operator: ", exampleTypeRule.rule_type.operator
        self.assertEqual(6, exampleTypeRule.rule_type.value)
        print "value: ", exampleTypeRule.rule_type.value

        

    def test_SeveralTypeRules(self):
        rule1 = parse ("r1 = typeRule Categories [a, b, c, e,] together must \
            have less_than 7 inputs.", genericRule)
        rule2 = parse ("r2 = typeRule Categories [a, b,] together must \
            have less_than 8 inputs.", genericRule)
        pass

# automatically run test case when file is invoked 
if __name__ == '__main__':
    unittest.main()
