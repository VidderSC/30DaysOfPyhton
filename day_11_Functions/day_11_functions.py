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
print(add_two_numbers())
print()


def generate_full_name_two():  # Declaring the function
    first_name = 'Vidders'
    last_name = 'SC'
    space = ' '
    full_name = first_name + space + last_name
    return full_name  # We are returning the full name


print(generate_full_name_two())  # Calling the function


def add_two_numbers_two():  # Declaring the function
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers_two())  # Calling the function
print()

# Functions with Parameters
# If our function takes a parameter we should call the function with it


def greetings(name):
    message = name + ', welcome to Python in 30 days!'
    return message


print(greetings("Vidders"))


def add_ten(number):
    ten = 10
    return number + ten


print(add_ten(59))


def square_number(number):
    return number * number


print(square_number(2))


def sum_of_numbers(number):
    total = 0
    for i in range(number+1):
        total += i
    return total


print(sum_of_numbers(69))
print()


def generate_full_name_three(first_name, last_name):
    space = " "
    return first_name + space + last_name


# If we have more than one argument, we need to respect the order of
# the arguments when passing them
print(generate_full_name_three("Vidders", "SC"))

# If we pass the arguments as Key and Value, the order doesn't matter.
print(generate_full_name_three(last_name="SC", first_name="Vidders"))
print()


def calculate_age(current_year, birth_year):
    return current_year - birth_year


print(f'Age: {calculate_age(2023, 1954)}')


def weight_of_object(mass, gravity):
    # In order to add the 'N' at the end, we need to convert to string
    weight = str(mass * gravity) + " Newtons"
    return weight


print(f"Weight of an object: {weight_of_object(100, 9.81)}")
print()

# Functions with default parameters
# We can define functions that if no parameters are specified, then
# the default values will be used.


def greet(name="Homer"):
    return "Hi " + name


print(greet())
print(greet("Vidders"))
print()

"""
# Arbitrary number of arguments
If we don't know the number of arguments we will pass to our 
function, we can create a function which can take an arbitrary 
number of arguments by adding * before the parameter name.
"""


def sum_all_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all_numbers(2, 3, 5, 9))
print()


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


generate_groups("A-Team", "Murdoc", "Hanibal", "Mr. T")
print()

# You can pass a function as an argument of another function


def square_num(num):
    return num * num


def do_something(fun, arg):
    return (fun(arg))


print(do_something(square_num, 3))