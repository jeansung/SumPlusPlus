# Project description and plan

## Motivation

**Background**  
In gymnastics, routines are composed of different moves. There are many different types of moves, and within each type of move, different “flavors” of that move. For example, take turns. There are half turns, full turns, 1 ½ turns, 2x turns, etc.  In an advanced level/ Olympic level, there is a lot choice when designing routines with regards to what types of moves are included and what difficulties of moves are chosen.

**What problem are you trying to address?**   
In a few words: creating a gymnasts' routine.  
Currently, a domain expert, usually the gymnast’s coach or some other knowledgeable person, creates routines for the gymnast, knowing his/her strengths  relating to specific skills in order to maximize the start value of the routine.  This person has a very intimate understanding of the Code of Points, a complex and lengthy document, which also changes every so often (4-8 years). This is an old fashioned, outdated way that requires a lot of overhead (i.e. from the complexity of code of points) and an automated tool could help the coach/domain person focus their efforts more on the gymnast.

In addition, at very competitive levels of gymnastics, every single point, every tenth of a point matters. If a gymnast wobbles during a move that was suppose to be connected, they must forfeit the bonus/points associated with the connection or risk falling off the apparatus (a very large deduction). After this, how can a gymnast continue with their routine? What are the alternatives? What can still be done? This could be a tool to help map possible search space, given a particularly risky pivot (not the right word, I’m looking for critical point? ) in the routine. 

**Why is a DSL the appropriate solution?**  
This problem has a very narrow scope, i.e. calculating a weighted sum with a set of constraints. There is not a need for a lot of the functionalities that a general purpose langauge may provide. In addition, by using, or creating a domain specific language, I can narrow the input methods specically for this problem to enhance the user experience and minimize errors. 

**Why is this project useful or interesting?**  
This project is useful, at least in the domain of creating gymnastics routinues for the reasons described. It could also be used for sports similar to gymnastics like dance. But beyond sports, there are a lot of general pupose applicatons for a tool that calculates a weighted sum based on a series of custom contraints. For example, a teacher that is trying to create a test. With a problem bank (of different topic questions of varying degree of difficulty), this tool would allow a teacher to create a test that has a quantifiable degree of diffuclty, especially in relative to other tests created with this tool. This was, a teacher could use numerical methods to differentiate tests; these are better metrics. 


## Language domain
**What is the domain that this language addresses?**  
* Primary: Artistic gymnastics at the elite level
* Secondary: teachers 

**Why is the domain useful?**   
This domain is useful because gymnastics is a personally important sport and teachers matter because their job is important to society.

**Who will benefit from this language?**  
* Gymnasts and coaches (primary benefactors and domain of this langauge)  
* teachers (secondary domain)

**Are there any other DSLs for this domain?**  
Not really. A weighted sum can be calcualted from an excel spreadsheet. There doesn't really exist anything that does both the weighted sum and the checking against constraints.*

*Note: My answer to this question is from approximately ~45 minutes google searching for things like 
* "weighted sum constraint tool"
* "wegihted sum with constraint"  
* "test creation tool for teachers"

I did find test creation tools online for teachers, for example, [here](https://www.easytestmaker.com/), [here](http://www.schoolhousetech.com/Test/), and [here](http://www.quizinator.com/). Some of these tools do provide the option to categorize different types of problems with tags, but none of these tools are concerned with making tests that incorporate custom constraints  or using numerical methods to analyze the test's properities. 

**If so, what are they, and how might they influence your language design and implementation?**  
Not applicable becaue of my answer to the previous question.

## Language design
**If you had to capture your DSL's design in one sentence, what would it be?**  
Takes a set of (type, difficuly) pair and check it against a set of rules to see if the input is consistent against the rules. 

**What constitutes a program in your language?**  
A program is a set of (type, difficulty) pairs and a set of one or more rules. 

**What happens when a program runs?**  
When a program runs, the inputs and the rules are cross checked to see if the state is consistent or not. 

**What kinds of input might a program take, and what kinds of output might it produce?**  
The inputs that the program will take are one or more of type and difficulty pairs, i.e. (type, difficulty). The output might be consistent/not consistent (a boolean?).  

**Are there data or control structures that you know will be useful?**  
A data structure to store the pairs of type and difficulties - maybe an `array` of some sort. I will need to iterate over the input array, so maybe a `loop`. I will need to determine `if` consistency is followed, so maybe I will need a way of checking. 

**What kinds of things might go wrong in a program in this domain (e.g., syntax errors, compile-time errors, run-time errors)?**  
Like most langauges, there could be things that go wrong. The biggest thing I anticipate as an error is if users create contradictory rules. For example, if a rule that says that categories must sum to at least 10 and another rule that says those categories cannot sum to more than 9, it would be problematic. Of course, syntax error and other types of errors might happen.

**How might you design your language to prevent such errors or to clearly communicate the results of errors to the user?**  
I will design my language to encourage people to enter correct and consistent (i.e. non contradictory) rules whenever possible. The input formate for the types and difficult will be presented in a chart, similar to [this](https://docs.google.com/a/g.hmc.edu/drawings/d/1s66OigYr9tjV2eS_UL-D5rtic1B1mTxPinMK_0AyMF4/edit) so that users can selected which points they want with ease.Rules will be checked against each other as they are inputed so that impossible rules that are contradictory cannot be created.

As for syntax and compile time errors, I will try it out with users (i.e. farther down the line) to see what are the common errors and from there I will try to create sensible and helpful error messages. 


## Example computations  
**Describe some example computations in your DSL. These computations should describe what happens when a specific program in your DSL executes. Note that you shouldn't describe the syntax of the program. Rather you should describe some canonical examples that help someone else understand the kinds of things that your DSL will eventually be able to do.**

Here is an image that depicts a typical run of the program:
![](https://docs.google.com/drawings/d/1s66OigYr9tjV2eS_UL-D5rtic1B1mTxPinMK_0AyMF4/pub?w=960&h=720)

First, people input the frame of what they have- types and difficulities. Then they select the options which they want. After that, they can input the rules, at first selecting from a specific set and customizing based on the categories they selected. Then, when the program is executed in my DSL, the result will return as `consistent` or `inconsistent`. 

Here is a sample program of a more simple nature, a `Hello World` program, per say.
![](https://docs.google.com/drawings/d/1oSjX7MIUAJfmSEWhdJA7cH3WaUsSsQ8-Q_65wL1ZXeQ/pub?w=960&h=720)