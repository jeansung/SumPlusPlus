# Preliminary evaluation
Jean Sung  
due Sunday, November 30 @ 11:59pm Pacific  
worth (10%)

**What works well? What are you particularly pleased with?**
From start to end you can start with text files
I am pleased that it works from start to finish
pleased that it is not overly complicated
like the parser aljeandro's initial suggestion as well as his suggestions for improving the parser was very helpful in being able to extract what is usefrul fom the rule  


**What could be improved? For example, how could the user's experience be better? How might your implementation be simpler or more cohesive?**

More test cases for the parser
 A better front end. Right now everything has to be done from the terminal which is not the ideal UI
 text files have to be formatted exactly so 
 a web interface would definitely be more ideal (not planning on doing that because of time constraints, but that's the end stretch goal)
I need to and will include instructions 

implementation is pretty simple as it is
would help if I separated out the files (sub divisions of the program files folder) this is at least less visually a mess for what files are test files, parser files, main python files, helper files, output files


**Re-visit your evaluation plan from the beginning of the project. Which tools have you used to evaluate the quality of your design? What have you learned from these evaluations? Have you made any significant changes as a result of these tools, the critiques, or user tests?**

I said I planned to use user tests and self test with my original use cases to see if I could accomplish what I set out as a goal in the description md file

I have not done formal user tests but so far I have had my friends informally try out the tool, which is how I mainly evaluate the design. I will do the self tests with my two original use cases at the end when I am done with the functionality of the program 

I also ask about/ receive feedback on the design on a weekly basis from alejandro 

I have learned from this that 
instructions / sample programs are key to making it easy to use for new users 
From these tests, I learned that the types/values (i.e. the table file) is probably best inputted as one file (simpler is easier to manage) 

critiques from Alejandro was very helpful because he was able to suggest tools that made the engineering part of the project easier
user test from Sarah was helpful in showing me that I needed to include sample programs and instructions (she had this for her project and it was really effective) 

The main change is to make my program 2 fold
one part is creating the sandbox enviornment with the tables
the other part is creating the rules

**Where did you run into trouble and why? For example, did you come up with some syntax that you found difficult to implement, given your host language choice? Did you want to support multiple features, but you had trouble getting them to play well together?**

run into trouble with coding as my project evolved (i.e. not knowing the entire architecture upfront ) and coding in a way to make things work first 

which means a bit of messy cross connected files with increasingly unweidly files 

thus had to spentd time refactoring the code . recdedicing how the architecutre informs the code

I also had trouble with the feature of constraint consistency checker (i.e looking for contradictions)
linear programming 
which is advance
I know it is possible in matlab, but I am still working on getting it to integrate with python nicely 


**What's left to accomplish before the end of the project?**
Major:
integrate support for value rules
writing rules to excel files
constraints contradiction checking
create demo/ presentation 

Minor: 
more error checking 
include sample programs
write instructions for how to use, i.e. updated the readme file 
reorganize code and program files
package deliverables for user 
documentation / written deliverables due for project

**If you worked as a pair, describe how you have divided your labor and whether that division has worked well.**

work by myself 
some weeks had trouble finding time during the week to start the project
end up with 4+ hour blocks on Saturday/ Sunday to meet quota
meeting with prof ben during the week helps force me to think about what is upcoming and next for my project in a critical way earlier in the week
I also worked a fair bit over thanksgiving break, which helped. 