# Day 5 - 30DaysOfPython Challenge

# Lists
"""
There are four collection data types in Python :    
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

A list is a collection of different data types which is ordered and modifiable(mutable). 
A list can be empty or it may have different data type items.
"""

# We can create a list in two different ways:
# - Using list() or [] (Both lists will be empty)
empty_list1 = list()
empty_list2 = []

# - Adding initial values. We can also use len() to find the length of a list.
fruits = ['banana', 'orange', "mango", "lemon", "lime", "apple"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yoghurt"]
web_techs = ["HTML", "CSS", "JS", "React", "Redux", "Node", "MongoDB"]
countries = ["Spain", "Finland", "Denmark", "Sweden", "Norway", "Finland"]

print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web Technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
print()

# Lists can have items of different data types
lst = ["Vidders", "SC", 69, True, {"country": "Spain", "city": "Malaga"}]
print(lst)

"""
We can access lists using positive and negative indexing

fruits = ['banana', 'orange', "mango", "lemon"]
pos_index     0         1        2        3
neg_index    -4        -3       -2       -1
"""
first_fruit = fruits[0]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)
print()

# Unpacking list items
item0, item1, item2, *rest = fruits
print(item0)
print(item1)
print(item2)
print(rest)
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item0, item1, item2, *other, item8, item9 = numbers
print(item0)
print(item1)
print(item2)
print(other)
print(item8)
print(item9)
print()

# Slicing a list
all_fruits = fruits[0:7]  # Returns all the fruits until 7 without counting it
print(all_fruits)
all_fruits = fruits[0:]  # Returns all the fruits, using positive indexing
print(all_fruits)
all_fruits = fruits[-6:]  # Returns all the fruits, using negative indexing
print(all_fruits)
# We are skipping the first item and limiting until the 2nd index
orange_mango = fruits[1:3]
print(orange_mango)
lemon_lime = fruits[3:5]
print(lemon_lime)
print(numbers)
skipping_one = numbers[::2]  # We are skipping 1 item everytime
skipping_three = numbers[::4]  # We are skipping 3 items now
print(skipping_one)
print(skipping_three)
turned_around = numbers[::-1]
print(turned_around)
print()

# Modifing lists
print(fruits)
fruits[0] = "avocado"
print(fruits)
last_index = len(fruits) - 1
print(last_index)
print(fruits[last_index])

# Checking for an item in a list
does_exists = "avocado" in fruits
print(does_exists)
does_exists = "banana" in fruits
print(does_exists)
print()

# Adding and inserting items to a list
fruits.append("banana")
print(fruits)
does_exists = "banana" in fruits
print(does_exists)
print()
fruits.insert(2, "strawberry")
print(fruits)

# Removing items from a list, we can use:
# .remove() = Removes an specified item by the name.
# .pop() = Removes an specified item by the index or the last if left blank.
removed = fruits.remove("lime")
print(removed)  # Remove doesn't returns the deleted item
print(fruits)
poped = fruits.pop(0)
print(poped)  # Pop returns the deleted item if we assign to a variable
print(fruits)
fruits.pop()
print(fruits)

# Deleting items and the list
del fruits[0]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
# print(fruits)  # NameError: name 'fruits' is not defined
print()

# We create the fruits list again, we copy it and then we clear it
fruits = ['banana', 'orange', "mango", "lemon", "lime", "apple"]
fruits_copy = fruits.copy()
print(fruits)
print(fruits_copy)
fruits.clear()  # With clear() we empty the list without deleting the variable
print(fruits)  # now it's empty
print(fruits_copy)
print()
fruits = fruits_copy.copy()

# We can join lists also
positive_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
negative_numbers = [-9, -8, -7, -6, -5, -4, -3, -2, -1]
zero = [0]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits_vegetables = fruits + vegetables
print(fruits_vegetables)

# Using the extend() method allows to append list in a list
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
print(num1)
print(num2)
num1.extend(num2)
print(num1)
print()

# Counting items in a list
print(fruits.count("orange"))
ages = [43, 19, 22, 43, 30, 19, 43, 22]
print(ages.count(43))
print()

# Finding the index of an item in a list
print(fruits.index("mango"))
print(ages.index(19))  # Will only find the first occurrence
print()

# We have seen how to reverse a list using the slicing method,
# which doesn't affect the order within the list.
# We can also use reverse() to reverse the items,
# but affects the order of the items in the list.
print(fruits)
fruits.reverse()
print(fruits)
print()
# Finally we car sort our lists
# To sort lists we can use:
# - sort()   = Reorders the list of items in ascending order and
#              modifies the original list.
#              Using reverse=True, will sort in descending order.
# - sorted() = Returns the list of items in ascending order
#              without modifying the original list.
#              Using reverse=True, will sort in descending order.

print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(fruits)
print()
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
