from functools import reduce

# Day 14 - 30DaysOfPython Challenge

# Higher Order Functions - HOF
"""
Python allows you to perform the following operations on functions:
- A function can take one or more functions as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

In this section, we will cover:
1. Handling functions as parameters
2. Returning functions as return value from another functions
3. Using Python closures and decorators
"""

# Function as a parameter


def sum_numbers(num_lst):  # Normal function
    return sum(num_lst)


def higher_order_function(fun, lst):  # Takes function as a parameter
    summation = fun(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)
print()
# Function as a return value


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function1(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute


# Below you will see that I have used '# type: ignore'.
# If I don't use it, the IDE will return a problem with the code
# as Pylance does not allow an object with Type 'None' to be called.
result1 = higher_order_function1("square")
print(result1(3))  # type: ignore
result1 = higher_order_function1("cube")
print(result1(3))  # type: ignore
result1 = higher_order_function1("absolute")
print(result1(-3))  # type: ignore
print()

# Python closures
"""
Python allows a nested function to access the outer scope of 
the enclosing function. This is is known as a Closure.

A closure is created by nesting a function inside another encapsulating 
function and then returning the inner function.
"""


def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add


closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))
print()

# Python decorators
"""
A decorator is a design pattern in Python that allows a user to add new 
functionality to an existing object without modifying its structure. 

Decorators are usually called before the definition of the 
function that you want to decorate.

To create a decorator function, 
we need an outer function with an inner wrapper function.
"""


# Decorator functions are HOF that take functions as parameters
def uppercase_decorator(fun):
    def wrapper():
        func = fun()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
def greeting():
    return "Welcome to Python!"


print(greeting())
print()

# Applying multiple decorators to a single function


def split_string_decorator(fun):
    def wrapper():
        func = fun()
        splitted_string = func.split()
        return splitted_string
    return wrapper


# Order with decorators is important in this case as
# the upper decorator will not work with lists

@split_string_decorator  # Second to execute
@uppercase_decorator  # First to execute
def greeting1():
    return "Welcome to Python!"


print(greeting1())
print()

# Accepting parameters in Decorator functions


def decorator_with_parameters(f):
    def wrapper_accepting_parameters(p1, p2, p3):
        f(p1, p2, p3)
        print(f"I live in {p3}")
    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(fname, lname, c):
    print("My name is {} {} and I'm learning Python.".format(fname, lname, c))


print_full_name("Vidders", "SC", "Spain")
print()

# Python Built-in HOF
"""
Some of the built-in higher order functions that we cover in this part are
- map():
    The map() function is a built-in function that takes 
    a function and iterable as parameters.
- filter():
    The filter() function calls the specified function which 
    returns boolean for each item of the specified iterable (list). 
    It filters the items that satisfy the filtering criteria.
- reduce():
    The reduce() function is defined in the functools module and 
    we should import it from this module. 
    Like map and filter it takes two parameters, a function and an iterable. 
    However, it does not return another iterable, it returns a single value.

A Lambda function can be passed as a parameter and the best use case of 
lambda functions is in functions like map, filter and reduce.
"""

# Examples of map()
# Syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]

# we will be using functions already declared previously above
numbers_squared = map(square, numbers)
print(list(numbers_squared))

# using a lambda
numbers_squared1 = map(lambda x: x ** 2, numbers)
print(list(numbers_squared1))
print()

numbers_str = ["1", "2", "3", "4", "5"]
print(numbers_str)
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ["Vidders", "Pinky", "Richy", "Luna"]


def change_to_upper(n):
    return n.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

# using a lambda
names_upper_cased1 = map(lambda x: x.upper(), names)
print(list(names_upper_cased1))
print()

# Examples of filter()
# Syntax: filter(function, iterable)


def is_even(num):
    return num % 2 == 0


even_numbers = filter(is_even, numbers)
print(list(even_numbers))


def is_odd(num):
    return num % 2 != 0


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))


def is_long_name(name):
    return len(name) > 6


long_names = filter(is_long_name, names)
print(list(long_names))
print()

# Examples of reduce() - We need to import before using it
# from functools import reduce
# Syntax: reduce(function, iterable)


def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
# We didn't use print(list(total)) because reduce() returns a single value
print(total)
