##### What are one or more things that you like about this project? What's exciting?

I like the idea of giving the power of computaters to those a group of people who wouldn't otherwaise have it, namely gymnists and their coaches. There are lot of things we do that a computer could do much better, so any project like this one that helps people put those aspects of their work into a computer so they can focus on other aspects is exciting. 

##### What's the balance of language design vs sheer programming / engineering in this project?

It seems that the domain is specific enough that the programming / engineering won't be the focus. The focus will be on how to create a user friendly experience in the way the language is designed. I guess as more work is put on making it easy to use, though, that there will be more engineering challenges. For instance, the "all else" feature now forces an ordering to the rules. That adds a level of complexity to the DSL itself.

##### How can the project maximize the time spent on language design? How to focus on interesting, possibly new ideas?

As I understand it, Excel is actually capable of doing the entire thing. It would look ugly and be hard for a non-excel expert to do, but creating a table for the input and writing constraints that compose together is not out of Excel's scope. I'd be happy to show you how if you're interested.

Given that, I think the interesting design decisions will be in the language used to input the contraints. The list of (type, point) pairs is simple enough to input (many ways to do that), but the contraints are usually hard to write for a non-programmer. If the goal is to make this useful for a gymnist or coach, then the language will need to support some featuers that do a lot for a little. Such as the "all else" piece of the constraint. There is a finite set of things that one needs to do in the creation of constraints for this domain. So I think there could be a fair amount of design decisions in creating a languag that makes those all accessible in an intuitive way (no small feat). 

##### What are some interesting language design questions that the work will have to answer? In other words, what are the design challenges? Which design problems' solutions are you looking forward to hearing about at the end of the project?


Much as the same answer I just gave above. The challenge will come in the DSL for contraint writing. I'm interested to see how it will be easy to use for a non-programmer. I think a lot of care will need to be taken to give very useful error messages, both for syntax errors and inconsistency errors. I think creating a checker that can tell if a set of constraints is contridictory or constistent and then let the user know where it was self-contradicting would be both extremely useful and very challenging to do well. But I think these types of things will be necessary for the target users you've choesn.

##### What are the primitives in this language?

Type of move
Point Values
Numbers used in contraints

Pretty simple language with complicated design decisions. I think this was a great choice for a DSL.

##### Do you know of any libraries, languages, or projects that might help this project?

I know Excel can do all of the things, so it might actually be helpful to see that. But that won't contribute directly to the language. I'm working with Salesforce and would be happy to show you how they let you build contraints. It is more focused on input though, rather than changing the language. But they might give some ideas on how to simplify the input process.

This might be a personal preference, but since this is intended for non-programmers, I might think about making it a webservice. It could make it more interactable. If that appeals to you, that might limit the choices for host language to one that is compatible with a web service or at least require some research.

