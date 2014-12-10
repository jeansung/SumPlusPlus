It should be noted that to use the virtual environment that was installed by the bootstrap the user has to type `source venv/bin/activate`. I suggest making a script like my `mindsketch.sh` one that just activates the virtual environment and then calls run.py. It could look like this:

```bash
source venv/bin/activate
python run.py
```

`nosetests` also works instead of using the unittest discovery directly.

Installation went perfectly as did the samples.

It was unclear at first that Table Creation and Rule Generation require the files to already be created. I thought they would assist in their creation by at least creating the file if it didn't exist and maybe even accept user input to create the file with. Maybe a thing for the future or to fake int he demo.

After that it was easy enough to create files.

It might be nice to ignore/remove the whitespace in the tables declaration files. I'd like to be able to put spaces after the commas without them being put in the excel table.

The error messages aren't that great. For example if I use a name in the rules that wasn't declared in the table I get:

```
Traceback (most recent call last):
  File "run.py", line 84, in <module>
    if __name__ == "__main__":main()
  File "run.py", line 73, in main
    nameFormulaPairs = generateExcelFormulas(parsedRules)
  File "/Users/jarthur/Projects/SumPlusPlus/source/generateConstraints.py", line 62, in generateExcelFormulas
    (name, formula) = createTypeRule(r)
  File "/Users/jarthur/Projects/SumPlusPlus/source/generateConstraints.py", line 83, in createTypeRule
    row = globals.typeRowMapping[t]
KeyError: u'potatos'
```

It does at least tell me that "potatos" is wrong, but I don't know where it was wrong, like which file or which line.
It is made harder because the table file and the rules file are seperate, so I can't see them side by side for easy spot checks either. If they were together it would be easier to make a parser that gives better error messages. I'm not sure the seperation gives any useful features over the confusion it causes. Unless your use case involves the same table being used for many different sets of rules. I could see that happening, but not sure if it is a common enough use case...

A comment on rule creation syntax: could use pyPEG's built in `csl` or comma seperated list. Then it look like this:

```python
class TypeList(List):
	grammar = "[", csl(word) "]"
```

Here's an example use:
```shell
>>> from __future__ import unicode_literals, print_function
>>> from pypeg2 import *
>>> class TypeList(List):
...     grammar = "[", csl(word), "]"
... 
>>> t = parse("[hello, world, yup]", TypeList)
>>> t
TypeList([u'hello', u'world', u'yup'])
```


Overall it seems like you have a working prototype. I look forward to seeing what the final vision of the project is in your final demo.

