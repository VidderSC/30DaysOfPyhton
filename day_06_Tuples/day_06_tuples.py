# Day 6 - 30DaysOfPython Challenge

# Tuples
"""
A tuple is a collection of different data types which is ordered and 
unchangeable (immutable). Tuples are written with round brackets, (). 
Once a tuple is created, we cannot change its values. 
We cannot use add, insert, remove methods in a tuple because it 
is not modifiable (mutable). Unlike list, tuple has few methods. 
Methods related to tuples:
tuple() - To create an empty tuple
count() - To count the number of a specified item in a tuple
index() - To find the index of a specified item in a tuple
+ operator - To join two or more tuples together and create a new tuple
"""

# Creating an empty tuple, there are two ways:
empty_tuple = ()
empty_tuple = tuple()

# Creating a tuple with initial values:
tpl = ("item1", 'item2', 'item3')
fruits = ("banana", "orange", "mango", "lemon")

# Tuple length
print("fruits:", fruits)
print("The length of the tuple is:", len(fruits))
print()

# We can access the tuple with positive and negative indexing, just like with lists.
first_item = fruits[0]
second_item = fruits[1]
last_item = fruits[-1]
print("first_item:", first_item)
print("second_item:", second_item)
print("last_item:", last_item)
last_index = len(fruits) - 1
print("last_index:", last_index)
print()

# Slicing using positive and negative indexes
all_fruits = fruits[0:4]    # all items
all_fruits = fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item the index 3
orange_to_the_rest = fruits[1:]

all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

# Changing Tuples to Lists and viceversa
fruits_list = list(fruits)
fruits_tuple = tuple(fruits_list)

# Checking an item in a Tuple, using "in" will return a boolean value
print("orange" in fruits)
print("apple" in fruits)
print()

# Joining Tuples
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_veggies = fruits + vegetables
print(fruits_and_veggies)

# Deleting Tuples
# It is not possible to delete a single item of a tuple,
# but it is possible to delete the tuple itself using "del"

del fruits_tuple
# print(fruits_tuple)  # NameError: name 'fruits_tuple' is not defined