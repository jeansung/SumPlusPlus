## UI Design & Language Notes  
Now that I have figured out that the majority of the engineering or programming work can be done by Excel, I need to figure out a more intuitive way to input the 2 parts of my language, the table of (type, input) pairs and the set of constraints. 

I might be able to get away using excel for entering the table of (type, input) pairs because of the colloquial familiarity of non programmers with Excel. However, although Excel does support the creation of rules with logical IF, it is not in a programmer friendly way. In addition, I want to create something where there is more limited functionality. 

The major things I need from UI consideration is a way to **create table**, **create rules**, **check consistency**. 

## Some confusion
I understand what we did for the internal and external lab in Scala, but I am not sure about how what I am doing fits in this model. I don't think Excel quite cover all of what my language encompasses because I will probably doing another type of user facing interface for inputing the rules, thus the language I am building won't be an internal DSL. I plan to resolve this trouble with visualizing the engineering part of it by meeting with Prof Ben on Tuesday. 


## Java related options
My main idea is to have an excel like interface for creating the [table](http://docs.oracle.com/javafx/2/ui_controls/table-view.htm) and then a java Applet that will assist in rule creation / running the program to check for consistency. 

The main concern of this method is how I would get Excel to 

The benefit of this idea is the Java Applet will be very portable because Java runs on many machines. In fact, if the table itself is defined elsewhere, then re running the applet means that you can start with a table and perhaps rules, instead of redefining it again multiple times. 

## Other ideas  

Maybe have a way to lay everything out statically then run it to check? A big feature I want is live updating, if that is possible.

Excel does have support for drop down menus and [controls](http://support.microsoft.com/kb/291073) so I could potentially create a useable front end in excel. 

Another way to do this would be embedding the excel sheet in some sort of web interface. I know this is possible and here are some possible sources
* [possible source ](http://agsci.psu.edu/it/how-to/making-excel-interactive-on-the-web)
* [another possible source](http://office.microsoft.com/en-us/excel-help/put-excel-data-on-a-web-page-HP005256150.aspx)

I also plan to support limiting the scope of the table in the future (i.e. if for certain types certain difficulty values are not allowed). 