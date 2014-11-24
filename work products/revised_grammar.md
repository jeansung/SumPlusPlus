Jean Sung  
DSL Final Project   
Rule generation grammar 

```
// primitive things 
letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" ;
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
decimal_point = "." ;
decimal_value = { digit }, decimal_point, { digit } ;

// name is an identifier for a rule
name = { letter } ;

// Total inputs must be an int
// Total of the value may be a double
totalInputs = { digit } ;
totalValues = { decimal_value } ;

// A type is any word (i.e. made up of letters)
type = { letter }; 
types:= { type }

// Other rule parts
operator = < | = | > ;
relation = "each" | "together" ;

// Rule types 
typeRule = Categories (types) (relation) must have (operator) (totalInputs) inputs. ;
valueRule = Categories (types) (relation) must sum to (operator) (totalValues). ;
genericRule = typeRule | valueRule ;
Rule = name,  "=", genericRule;
Rules = {Rule} ; 

Notes: 
* Rules are defined relative to a table. Thus, it is assumed that the type
must be defined in the table. The rules are written with a check for existence
of types in a table file. Rules therefore must be backed by a table.
```