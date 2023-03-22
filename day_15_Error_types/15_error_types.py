# Day 15 - 30DaysOfPython Challenge

# Pyhton Error Types
"""
If our code fails to run, the Python interpreter will display a message 
containing feedback with information on where the problem occurs and the type 
of error. Sometimes could gives us suggestions on a possible fix.

The most common error types are:
- SyntaxError: We forget to enclose with parenthesys.
    print "Hello World!"
    # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

- NameError: We try to print a variable that haven't been defined:
    print(age)
    # NameError: name 'age' is not defined

- IndexError: We go out of range on the index of an array.
    numbers = [1, 2, 3, 4, 5]
    print(numbers[5])
    # IndexError: list index out of range
    
- ModuleNotFoundError: We try to import a module that doesn't exist or is not installed.
    import maths
    # ModuleNotFoundError: No module named 'maths'
    
- AttributeError: We try to call a function that doesn't exist in the module
    import math
    math.PI
    # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

- KeyError: The key we use doesn't exist in the dictionary
    users = {'name':'Vidders', 'age':69, 'country':'Spain'}
    users['name']  # Vidders
    users['county']
    # KeyError: 'county'

- TypeError: We cannot add numbers to a string, as they are 2 different types.
    print(4 + "3")
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

- ImportError: We try to import a function that doesn't exist in a module 
    from math import power
    # ImportError: cannot import name 'power' from 'math' (unknown location)

- ValueError: We cannot change an string to number cause it cotains an 'a' in it.
    number = int("12a")
    # ValueError: invalid literal for int() with base 10: '12a'

- ZeroDivisionError: We cannot divide a number by zero.
    print(10/0)
    # ZeroDivisionError: division by zero
"""

# print "Hello World!"

# print(age)

# numbers = [1, 2, 3, 4, 5]
# print(numbers[5])

# import maths

# import math
# math.PI

# users = {'name':'Vidders', 'age':69, 'country':'Spain'}
# users['name']
# users['county']

# print(4 + "3")

# from math import power

# number = int("12a")

# print(10/0)
