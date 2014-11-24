## Prototype

Due November 23rd, 2014 

### Quick Refresher on my Language
As a quick reminder, I am building a tool that allows a user to specify a custom environment for creating and checking the feasibility of constraints. This means that a user will input types and values, as well as a set of constraints, and then they will receive a sandbox Excel file to play around in, checking to see how various configurations do/do not follow the rules. 


### Current State of the Project
Here is an architectural overview of what I imagine the language will look like: 
![](https://github.com/jeansung/project/raw/master/work%20products/system_architecture_picture.jpg)

### Accomplished thus far
* deciding on the control flow for the program, i.e. that the end result is an Excel Sandbox file
* interface Python with Excel to create the initial table from types, values input
* created the secondary, intermediate tables that summed the row/cols (used for final calculations and overall restrictions)
* demonstrate that using Python to create rules is possible (for limited hard coded cases)

The main push of this project is creating a good language for specifying and inputting the rules.   
* I have created a grammar for it. 
* I have implemented a parser with some preliminary test cases for it.
 

### Remaining Goals 
Between now and when the final project and presentation is due, there are 3 weeks (2.5 because this week is Thanksgiving). My big goals are 
* I need to connect the parser to a back end functionality (i.e. connect the parser to real rules)
* I need to implement a check for consistency 
* Error checking, testing, and wrapping everything together for a good user interface/ flow 

### Things to Check out! 

* Revised grammar, file in `work products` directory
* Parser and Parser Test in `program files/parsing` directory
* Sample Excel Sandbox Table, `dsl_prototype.xls` in the `program files` directory 
* Video walkthrough of the prototype, [here](https://drive.google.com/a/g.hmc.edu/file/d/0B9z84Or5GzOnaXhDMXFVLUpaOUk/view?usp=sharing)
