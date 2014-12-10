Small technicality on your grammar. The grammar doesn't current;y allow "value" to be decimal numbers. I know for summing point values, that decimal numbers are possible (if not common). And I know that for summing how many inputs is always whole numbers. You might want to seperate those two types of values.

The grammar seems solid. Since the point of writing rules is to make it easy to write, you might think about supplying some choices in the words, some syntactic sugar if you will. You can do this last of course, but I would keep in mind what types of syntactic sugar you might want to allow. E.G. `each must` as a possible replacement for `individually`. `categories (A, B, C) each must sum to 3 points`. There are lot of things like that, so I would just keep in mind what possible substitues you might add in the implementation of the parser to make it easier to add later.

From what I can see the grammar will be relatively easy to parse information out of. You will need to come up with IR, though. I don't know if you've decided on what kind of parser to use or if you've decided on external vs internal. Either way, look into some python parsers, like pyPEG2, and see the format of the output. It's heavy in tuples and list usually. And see if you can make your Python code run off of a predefined AST, python style. And then see if you can begin to create that from what you parse from the user.

I imagine since this is to be used by non-coders, you'll want an external DSL. One file, easy to parse the list of types (maybe comma seperated), list of values, and then each rule on a seperate line. Then running your program generates the proper excel file for them to use. This way, you can make nice only forms for people to use. The online form formats the input into the proper text file and your code will output an excel file for them to download. That seems like a good end goal.

To keep things simpler on the implementation side, you might consider python parsers and AST stuff over Scala to keep to one language. Your language is simple enough that I don't think there will a terrible learning curve. From what I've seen, pyPEG2 will work for you. There are plenty of other.


Comment on your code so far.The file is getting big and fast, and many of the methods are utility methods. You might consider seperating it into multiple files soon to keep managable for yourself.