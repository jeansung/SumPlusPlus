# Preliminary evaluation
Jean Sung  
due Sunday, November 30 @ 11:59pm Pacific  
worth (10%)

**What works well? What are you particularly pleased with?**
Right now, you can run the full program from start to finish. I am pleased that all the pieces fit together. I am also happy that the parser is not overly complicated, thanks to Alejandro's initial suggestion and help with improving the parser (so that I could actually extract what is useful from the rule).

**What could be improved? For example, how could the user's experience be better? How might your implementation be simpler or more cohesive?**

I could have more test cases for the parser. A better front end would be nice. Right now everything has to be done from the terminal is not the ideal UI. The text file has to also be formatted exactly so. A web interface would be more ideal (but I am not planning to do this because of time constraints). The biggest and simplest improvement I could make is to include the instructions for running it. 

The implementation is pretty simple as it is. It would definitely help if I separated out the files (sub divisions of the program file folder)- this would mean at least less visually of a mess for what files are test files, parser files, main python files, helper files and output files. 


**Re-visit your evaluation plan from the beginning of the project. Which tools have you used to evaluate the quality of your design? What have you learned from these evaluations? Have you made any significant changes as a result of these tools, the critiques, or user tests?**

I said I planned to use user tests and self test with my original use cases to see if I could accomplish what I set out as a goal in the `description.md` file. I have not done formal user tests but so far I have had my friends informally try out the tool, which is how I mainly evaluate the design. I will do the self tests with my two original use cases at the end when I am done with the functionality of the program. I also ask about/ receive feedback on the design on a weekly basis from Alejandro. Also the user test from Sarah was helpful. The feedback from these sessions showed me sample programs, instructions are key to making it easy to use for new users. Also, the type/values (i.e. the table file) is probably best inputted as one file (simpler is easier to manage). 

In addition, the critiques from Alejandro were very helpful because he was able to suggest tools that made the engineering part of the project easier. The main change that I made to program as a result of these critiques is two fold: creating the sandbox environment with the tables, creating the rules separate from the table (still dependent on the table but now in a separate run). 


**Where did you run into trouble and why? For example, did you come up with some syntax that you found difficult to implement, given your host language choice? Did you want to support multiple features, but you had trouble getting them to play well together?**

I ran into the trouble with coding as my evolved (i.e. not knowing the architecture upfront) and coding in a way to make things to work first. This meant a bit of messy code and cross connected files with increasingly unwieldy dependencies. Thus, I had to spend time refactoring the code, and re deciding how the architecture informs the code. 

I also had some trouble with the feature of including a constraint consistency checker (i.e. looking for a contradiction within the rules). The solution is linear programming, which I now know is something that can be done in MatLab. I am still looking for a Python supported version. 

**What's left to accomplish before the end of the project?**

**Major:**
* writing the rules to Excel files 
* constraints and contradiction checking
* create demo and presentation 


**Minor:**  
* More error checking
* include sample programs
* write instructions for how to use (i.e. update the `README` file)
* reorganize code and program files
* package deliverables for the user
* documentation / written deliverables for the project  

**If you worked as a pair, describe how you have divided your labor and whether that division has worked well.**

I have been working by myself. Some weeks I had trouble finding the time during the week to start the project. I ended up having to do 4+ hour blocks on Saturday/ Sunday to meet the quota of 9 hours/  week. I started meeting with Prof Ben during the week and this helps force me to think about what is upcoming for my project in a critical way earlier in the week. I also worked a fair bit over Thanksgiving break. 