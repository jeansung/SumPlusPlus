# Language design and implementation overview

## Language design
*Be sure to answer the following questions and note any changes from your original design:*  

**How does a user write programs in your language (e.g., do they type in commands, use a visual/graphical tool, speak, etc.)?**

The part of my program that a user creates is the tables (what types and what difficulties) and the rules (i.e. the constraints). I will use a simple text file for the types and possible values, and initially text for creating the rules, with a specified grammar and probably in a template format. 

A stretch goal of mine is to have a GUI interface for creating the rules, one which will enforce the grammar. 

This is different from the original design where the user did everything in the GUI interface. 

**What is the basic computation that your language performs (i.e., what is the computational model)?**

The computational model for language is consistency checking. This means that the basic computation that my language performs is a check to see if the set of rules for a specific table led to a contradiction or an impossibility (where any input in the table would err). This is pretty similar to the design I had originally envisioned. 


**What are the basic data structures in your DSL, if any?**

The basic data structures in my language is a tuple of (table, rules). The table is probably some sort of 2D array, and the rules are probably a list of rule objects (post parsing, probably a list of keywords).  

**How does a the user create and manipulate data?**

The user creates data by making a table file and then making a rule file. When the user is ready to manipulate the table, those files are run through a consistency/correctness checker. If everything is okay, then the output is an Excel file where the user has can manipulate the data and the consistent/not consistent will live update. 

This is different from the originally envisioned designed as mentioned earlier in this document. By separating the creation and manipulation part of the process, it makes the entire system more reusable. 


**What are the basic control structures in your DSL, if any? How does the user specify or manipulate control flow?**

There really is not any control structure or control flow in the language. This is because the user is manipulating data to see whether the output is consistent. There not a sense of a "program flow" so to speak when using my language.


**What kind(s) of input does a program in your DSL require? What kind(s) of output does a program produce?**

My DSL requires 2 files for input, a file that specifies the table and a file that specifies the rules. There is a 1 file output, which is an Excel file. 

I had originally envisioned no file input or output and instead, just having the user do everything in a GUI, saving possibly a preferred configuration as a text file. 
 
**Error handling: How can programs go wrong, and how does your language communicate those errors to the user?**

Programs can go wrong in two ways, badly formed table files in terms of syntax or inconsistent/contradictory rules. If the table files do not pass the initial check for correctness, I will let the user know what the correct form of the file is and where their file deviated from that. If the rules are contradictory, I will let the use know the first rule in the set that poses a contradiction or impossibility. This sort of error checking and feedback is similar to what I originally envisioned for my program. 


**What tool support (e.g., error-checking, development environments) does your project provide?**

My tool will support error checking as above noted, and there will be a sandbox environment to play with the table / custom constraints. My stretch goal includes a developer tool (like a GUI) for the creation of rules. 


**Are there any other DSLs for this domain? If so, what are they, and how does your language compare to these other languages?**

There aren't really any other DSLs or tools that does this. You could make a simple version of my tool completely in Excel but the difference is that what I am making has a more reusable model/cleaner interface. 

## Language implementation
*Give a high-level overview of the implementation decisions you've made, including:*

**Your choice of an internal vs. external implementation and how and why you made that choice.**

External implementation. I made this decision because I have a clear idea of what I want to do (what things I will allow) and starting from the ground up in terms of designing makes it easier to limit what the user can do (so less ways to make errors). 

Also, with what I have made, embedding the language as an internal implementation doesn't make it easier. 

**Your choice of a host language and how and why you made that choice.**

Python is my host language. I made this decision largely because 
* it interfaces with Excel
* easy to work with (a lot of libraries)

**Any significant syntax design decisions you've made and the reasons for those decisions.**

I had decided to make tables just a list of values and a list of rules (in a plain text file) to simplify the table creation process. 

A major syntax decision I made this week that is different from the original design is the development of a grammar for the rule creation, which is specified in `prelim_grammar.md` document. 

**An overview of the architecture of your system.**

<!--
TODO: Draw something for it and show the Semantics/ IR /Semantics  transition.
 -->

