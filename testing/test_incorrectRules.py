from rule_parser import *
import unittest


class TestParser(unittest.TestCase):
    def test_IncorrectRules(self):
        # cannot parse cross rules 
        with self.assertRaises(SyntaxError):
            parse ("type_rule = typeRule Categories [a] together \
             must have less_than 6 inputs.", valueRule)

        # Type rules may NOT have a float total
        with self.assertRaises(SyntaxError):
            parse ("type_rule = typeRule Categories [a] together \
                must have less_than 4.6 inputs.", genericRule)

        with self.assertRaises(SyntaxError):
            parse ("type_rule = typeRule Categories [a] together \
                must sum to less_than 7 inputs.", genericRule)

        # TypeList cannot be empty 
        with self.assertRaises(SyntaxError):
            parse("value_rule =  valueRule Categories [] each \
                must sum to greater_than 5.0.", genericRule)

# automatically run test case when file is invoked 
if __name__ == '__main__':
    unittest.main()