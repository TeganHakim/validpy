# validpy
It is a library that makes validation checks in python

```python
import validpy
validator = validpy.Validator()

user_num = input("Enter a number: ")
if validator.isInt(user_num):
    print("Thank you for your input")
else:
    print("Please enter a number")
```