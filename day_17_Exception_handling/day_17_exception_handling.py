# Day 17 - 30DaysOfPython Challenge

# Exception handling
"""
Python uses try and except to handle errors gracefully.

A graceful exit (or graceful handling) of errors is 
a simple programming idiom: 
A program detects a serious error condition and "exits gracefully",
in a controlled manner as a result.

Often the program prints a descriptive error message to a terminal or 
log as part of the graceful exit, this makes our application more robust.
The cause of an exception is often external to the program itself.

An example of exceptions could be: 
- An incorrect input, 
- Wrong file name, 
- Unable to find a file, 
- A malfunctioning IO device.

Graceful handling of errors prevents our applications from crashing.

We have covered the different Python error types in the previous section. 
If we use try and except, then it will not raise errors in those blocks.

Syntax:  # else and finally are optional

try:
    {block of code}
except:  # May or may not have a condition
    {execute this block of code when there's an exception}
else:
    {If there are no exceptions, will run this block of code}
finally:
    {Always run this block of code}

"""
Examples:

try:
    print(10 + "5")
except:
    print("something went wrong!")

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I will run if there are no exceptions')
finally:
    print('I alway run.')

""" 
# Packing and Unpacking arguments in Python
    We can use two operators:
        - * for tuples
        - ** for dictionaries
"""

# Example:


def sum_five_numbers(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]

# We could unpack a list to pass all the values as arguments by
# using *list_name as argument
print(sum_five_numbers(*lst))


def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old.'


dct = {'name': 'Vidders', 'country': 'Spain', 'city': 'Malaga', 'age': 69}
# We could unpack a dictionary to pass all the values as arguments by
# using **dictionaty_name as argument
print(unpacking_person_info(**dct))
print()
# Packing Lists


def sum_all(*numbers):
    s = 0
    for i in numbers:
        s += i
    return s


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))
print()
# Packing Dictionaries


def packing_person_info(**data):
    for key in data:
        print(f"{key}: {data[key]}")
    return data


print(packing_person_info(name="Vidders",
                          country="Spain",
                          city="Malaga",
                          age=69))
print()

# Spreading in Python - Like in JavaScript, spreading is possible in Python.

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
print()
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)
print()

# Enumerate
# If we are interested in an index of a list, we could use
# the 'enumerate' built-in function to get the index of each item on the list.

for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(nordic_countries):
    print("hi")
    if i == "Iceland":
        print(f"The country {i} has been found at index {index}")
print()

# ZIP - Sometimes we would like to combine lists when looping through them.

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veggies = []
for f, v in zip(fruits, vegetables):
    fruits_and_veggies.append({"fruit": f, "veg": v})

print(fruits_and_veggies)
print()


# Exercises: Day 17
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Spain', 'Ukraine']
print(names)
print("""
1. Unpack the first five countries and store them in nordic_countries, then 
store Spain and Ukraine in es, and ua respectively:
""")

*nordic_countries, es, ua = names
print(nordic_countries)
print(es)
print(ua)
