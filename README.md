# validpy
It is a library that makes validation checks in python

# Installation
```python
> pip install validpy
```
# Usage
```python
import validpy
validator = validpy.Validator()
# Checking user input
user_input = input("Choose an option (1, 2, 3, 4): ")
valid_choices = ["1", "2", "3", "4"];
if validator.isInput(user_input, valid_choices):
        print("Correct")
# Checking numbers or strings
number = 3
if validator.isInt(number):
    if validator.isEven(number):
        print("Even number)
    print("Odd number")
else:
    print("Thats not a number")
```