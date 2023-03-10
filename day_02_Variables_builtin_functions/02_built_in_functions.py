# Day 2 - 30DaysOfPython Challenge

# Built-in functions
""" 
The most commonly functions used in Python are:
print(), len(), type(), int(), float(), str(), input(), list(), dict(), 
min(), max(), sum(), sorted(), open(), file(), help() and dir().

Also you can see the complete list of built-in functions available in the 
Python documentation: https://docs.python.org/3.9/library/functions.html
"""

from math import pi


print('Hello, World!')          # prints the value in console
print(len('Hello, World!'))     # counts the characters, including spaces
print(type('Hello, World!'))    # checks the data type
print(str(10))                  # converts the number into a string
print(int('10'))                # converts the string into a number
print(float(10))                # converts the number into a float
# input('Enter your name: ')    # takes user input from console

# Python has got many reserved words and We do NOT use reserved words
# to declare our variables or functions.

print(min(10, 20, 30, 40, 50))  # Gives the minimum value
print(max(10, 20, 30, 40, 50))  # Gives the maximum value
print(min([10, 20, 30, 40, 50]))  # Takes a list and gives the minimum value
print(max([10, 20, 30, 40, 50]))  # Takes a list and gives the maximum value
print(sum([10, 20, 30, 40, 50]))  # It takes ONLY a list and returns the sum

# Variables
print()
"""
Python Variable Name Rules:
- Must start with a letter or the underscore character
- It cannot start with a number
- It can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Are case-sensitive (firstname, Firstname and FIRSTNAME) are different variables)
- Style guide recommeds that we use snake_case not camelCase, but will work anyway.

Examples:
- Valid variable names:
firstname
age
country
first_name
capital_city
_if  # In case we want to use a reserved word as variable, we start with underscore.
year_2021
year2021
current_year_2021
num1

- Invalid variable names:
first-name
first@name
first$name
num-1
1num

"""

# We can declare multiple variables and add the values in the same line.
first_name, last_name = 'Vidders', 'SC'
country = 'Spain'
city = 'Malaga'
age = 43
is_married = True
skills = ['Python', 'Java']
person_info = {
    'firstname': 'Vidders',
    'lastname': 'SC',
    'country': 'Spain',
    'city': 'Malaga'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print(f'Last name: {last_name}')
print(f'Last name length: {len(last_name)}')
print('Person information:', person_info)
print(f'Skills: {skills}')

# Data types:
'''
There are several data types in Python. To identify them we can use the built-in 
function "type" as we saw on the previous day.
I will ask you to focus on understanding data types very well as, when it comes to 
programming, it's all about data types.
# int       = 10
# float     = 3.14
# complex   = 1j
# bool      = True
# str       = 'Vidders'
# list      = [1, 2, 'Vidders', False]
# dict      = {'name':'Vidders','age':69,'is_married':True}
# tuple     = (1,2,3)
# set       = {9.18, 3.14, 2.7}  # It's declared like dict but without the colon.

Differences between List, Tuple, Set and Dictionary:
- List: 
    Ordered collection of data, indexed,
    Mutable (can be modified).
    Allows duplicates.
- Tuple:
    Ordered collection of data, indexed,
    Inmutable (can't be modified).
    Allows duplicates.
- Set:
    Unordered collection of data, un-indexed,
    Inmutable, but we can add new items,
    Does not allow duplicates.
- Dictionary:
    Unordered collection of data stored as "key:value" pairs, indexed
    Mutable (can be modified),
    Does not allow duplicate keys.
'''

# Casting: We can convert one data type to another.
print()

num_int = 10
num_float = float(num_int)
gravity = 9.81
int_gravity = int(gravity)
num_str = str(gravity)
first_name_to_list = list(first_name)

print('num_int =', num_int, 'and the type is:', type(num_int))
print('num_float =', num_float, 'and the type is:', type(num_float))
print(f'gravity = {gravity} and the type is: {type(gravity)}')
print(f'int_gravity = {int_gravity} and the type is: {type(int_gravity)}')
print(f'num_str = {num_str} and the type is: {type(num_str)}')
print(f"int(num_str) cannot be done because it's not an integer")
print(
    f'float(num_str) = {float(num_str)} and the type is: {type(float(num_str))}')
print(
    f'First name to list = {first_name_to_list} and the type is: {type(first_name_to_list)}')

# Numbers
"""
Number data types in Python:
- Integers: (negative, zero and positive)   Example: -3, -2, -1, 0, 1, 2, 3
- Floating Point Numbers (Decimals)         Example: -2.25, -1.0, 0.0, 1.1
- Complex Numbers                           Example: 1 + j, 2 + 4j, 1 - 1j
"""

# Exercises: Level 2
print()

# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(age))

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))
print(len(last_name))

# 3. Compare the length of your first name and your last name
print(len(first_name) > len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# 4a. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# 4b. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# 4c. Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
# 4d. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# 4e. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_two
# 4f. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# 4g. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# 5. The radius of a circle is 30 meters.
# 5a. Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = pi * (radius ** 2)
print(area_of_circle)
# 5b. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = (2 * radius) * pi
print(circum_of_circle)
# 5c. Take radius as user input and calculate the area.
radius = float(input('Enter the radius to calculate the area: '))
print(f'The area of the circle is = {pi * (radius ** 2)}')

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Enter your name: ')
last_name = input('Enter your last name: ')
country = input('Enter the name of your country: ')
age = int(input('Enter your age: '))
print(f"Hi {first_name} {last_name}, so you're from {country} and {age} years old?")
print('Bye!')

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
