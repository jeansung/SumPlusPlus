Its helpful when reading the code for the parser to have an updated grammar in a docstring at the top.

pyPEG parser objects can subclass more than just strings. They can also be given attributes using the attr method.
With this you might be able to make a more useful AST tree that is easier to grab meaningful data from.

Example changes to typeRule:

```python
class typeRule(List): 
	grammar = attr("typing", RuleType), "Categories", \
				attr("types", TypeList), attr("relation", Relation), "must", "have", \
				attr("op", Operator), attr("value", integerNumber), "inputs", "."
```

I removed blanks since whitespace removing is automatic. This isn't necessaryt o do, but is more useful for enforing that at least one space does exist and for prettier composing if you use compose().

Now see what you get:
```python
>>> p = parse("valueRule Categories [a, b, c,] each must have greater_than 5 inputs.", typeRule)
>>> p
typeRule([])
>>> p.typing
RuleType(u'valueRule')
>>> p.types
TypeList([u'a', u'b', u'c'])
>>> p.relation
Relation(u'each')
>>> p.op
Operator(u'greater_than')
>>> p.value
5
```

This AST object is much easier to use in constructing the Excel file that is your target. You have easy access to all the pieces you need.

It will help keep things consistent if, again, you add the grammar as a docstring to the top of the parsing file, but also add peices of the grammar to the testing file.

Pro-tip for using `unittest`. Name the file with the pattern `test_*.py` and it will be autodiscovered by `python -m unittest discover`. This becomes helpful when you split up tests between many files. Also, it will be autodetected by `nosetests` which is an addon to `unittest` that does a cool things for free, like only showing print messages for failed test...
