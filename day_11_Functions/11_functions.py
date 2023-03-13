# Day 11 - 30DaysOfPython Challenge

# Functions
"""
A function is a reusable block of code or programming statements designed 
to perform a certain task. 
To define or declare a function, Python provides the 'def' keyword. 
The function's code is executed only if the function is called or invoked.
"""

"""
# Declaring and Calling a Function
When we make a function, we call it declaring a function. 
When we start using the it, we call it calling or invoking a function. 
Functions can be declared with or without parameters.
It's standard leaving 2 empty lines before and after declaring a function.
"""

# Function without parameters


def generate_full_name():  # Declaring the function
    first_name = 'Vidders'
    last_name = 'SC'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()  # Calling the function


def add_two_numbers():  # Declaring the function
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()  # Calling the function
print()

# Function returning values - Part 1
# If it doesn't have a return statement will return 'None'.
print(generate_full_name())
print()


def generate_full_name():  # Declaring the function
    first_name = 'Vidders'
    last_name = 'SC'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())  # Calling the function


def add_two_numbers():  # Declaring the function
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())  # Calling the function
print()

# Functions with Parameters
# If our function takes a parameter we should call the function with it

