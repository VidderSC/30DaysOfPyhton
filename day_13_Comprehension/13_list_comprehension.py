# Day 13 - 30DaysOfPython Challenge

# List comprehension
"""
It's a compact way of creating a new list from a sequence.  
Also it's considerably faster than processing a list using the for loop.

# syntax
[i for i in iterable if expression]
"""

# Example:1
"""
If we want to change a string to a list of characters. 
There are a couple of methods that we can use:

# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

"""

language = "Spanish"
print(f"language = {language}")
print(f"type(language) = {type(language)}")
print()

lista = list(language)
print(f"lista = list(language)  # {lista}")
print(f"type(lista) = {type(lista)}")
print()

lst = [i for i in language]
print(f"lst = [i for i in language]  # {lst}")
print(f"type(lst) = {type(lst)}")

# Example 2 - Let's generate a list of numbers
print()

numbers = [i for i in range(11)]  # Numbers from 0 to 10
print(f"numbers = {numbers}")
print()

squares = [i*i for i in range(11)]
print(f"squares = {squares}")
print()

list_of_tuples = [(i, i * i) for i in range(11)]
print(f"list_of_tuples = {list_of_tuples}")
print()

# Example 3 - List comprehension combined with if expression

even_numbers = [i for i in range(21) if i % 2 == 0]
print(f"even_numbers = {even_numbers}")
print()

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(f"odd_numbers = {odd_numbers}")
print()

list_of_numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
print(f"list_of_numbers = {list_of_numbers}")
positive_even = [i for i in list_of_numbers if i % 2 == 0 and i > 0]
print(f"positive even numbers from the list = {positive_even}")
print()

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"three dimensional list = {list_of_lists}")
flattened_list = [number for row in list_of_lists for number in row]
print("flattened_list = [number for row in list_of_lists for number in row]")
print(f"flattened list = {flattened_list}")
print()

print("# Lambda function")
print("""
It's a small anonymous function without a name. It can take any number of 
arguments, but can only have one expression. 
We need it if we want to write an anonymous function inside another function.

# Creating a Lambda Function
We use 'lambda' keyword followed by a parameter(s), followed by an expression. 
Lambda function does not use return but it explicitly returns the expression.

# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
""")

print("# Lambda examples")
print("""
# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
Lambda Function Inside Another Function
Using a lambda function inside another function.

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
""")

print("# Your IDE might change your 'lambdas' to 'def' because of PEP8.")
print("""PEP8: Always use a 'def' statement instead of an assignment statement that 
      binds a lambda expression directly to an identifier.
      """)

