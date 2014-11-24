## Sample Python
```
>>> from enum import Enum
>>> class Color(Enum):
		red = 1
	   	green = 2
	   	blue = 3
```

## Notes on Nomenclature

* The class `Color` is an enumeration or an enum. 
* The attributes `Color.red`, `Color.green`, etc., are enumeration members (or enum members). 
* The enum members have names and values (the name of `Color.red` is `red` and the value of `Color.blue` is 3, etc.)

`