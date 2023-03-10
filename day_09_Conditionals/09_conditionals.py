# Day 9 - 30DaysOfPython Challenge

# Conditionals
"""
Python scripts are executed sequentially from top to bottom. 
The sequential flow of execution can be altered in two ways:

- Conditional execution: 
A block of one or more statements will be executed if a certain expression is true

- Repetitive execution: 
A block of one or more statements will be repetitively executed as long as 
a certain expression is true. 

In this section, we will cover 'if', 'else', 'elif' statements. 
"""

# If condition
a = 3
if a > 0:
    print('A is a positive number')
    
# If Else
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# If Elif Else
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
    
# If condition in one line
a = 3
print('A is positive') if a > 0 else print('A is negative')

# Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# We can avoid writing nested condition by using logical operator and.
# 
# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

