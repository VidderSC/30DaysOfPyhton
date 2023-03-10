# Day 7 - 30DaysOfPython Challenge

# Sets
"""
Set is a collection of items. 
The Mathematics definition of a set can be applied also in Python. 
Set is a collection of unordered and un-indexed distinct elements and
it is used to store unique items, and it is possible to find the union, 
intersection, difference, symmetric difference, subset, super set and 
disjoint set among sets.
"""

# Creating a set. We use {} or set()
set1 = {}
set2 = set()

# With initial values it would be:
fruits = {'banana', 'orange', 'mango', 'lemon'}

print("fruits:", fruits)
print("Length of 'fruits':", len(fruits))
print()

# To access an item in a set, we need to use a loop.

# Checking an item in a set
print("Does 'fruits' contain 'mango'?", "mango" in fruits)
print()

# Adding items to a set.
# Once a Set is created we cannot change any items but, we can add additional items.

# To add ONE item, we use .add
fruits.add("lime")
print(fruits)

# To add MULTIPLE items, we use .update and we pass it a list as an argument
fruits.update(["strawberry", "coconut"])
print(fruits)
vegetables = ('tomato', "potato", "cabbage", "onion", "carrot")
fruits.update(vegetables)
print(fruits)

# Removing items from a Set in different ways:
""" 
- .remove():
      We can remove an item from a set using .remove() method.
      If the item is not found .remove() will raise errors, so it is good
      to check if the item exist in the given set before using .remove().
- .discard():
      Doesn't raise any errors.
- .pop():
      This will remove a random item from the Set.
      We can assign the poped item to a variable.
- .clear():
      We use this to empty the Set.
"""

# fruits.remove("pineapple")  # Returns KeyError cause pineapple doesn't exists.
fruits.discard("pineapple")  # Doesn't do anything, not even returns an error.
print(fruits)
fruits.remove('onion')  # No error because "onion" is in the set.
print(fruits)
fruits.clear()
print("The content of fruits after .clear() is :", fruits)
del fruits
# print(fruits)  # NameError: name 'fruits' is not defined

# Converting a list to a set
fruits_lst = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits_set = set(fruits_lst)
print(fruits_set)  # Duplicated items were discarded and left only one of each.
print()

# Joining Sets
# We can join two sets using the union() or update() method
# - .union() will return a new set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

# - .update() Will insert a set into a given set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)  # st2 contents are added to st1
print(st1)
print()

# Finding intersection items
# .intersection() returns a set of items which are in both the sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers)
print(even_numbers)
print(f"This is the intersection: {whole_numbers.intersection(even_numbers)}")
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(f"The intersection of dragon and python: {python.intersection(dragon)}")
print()

# Checking Subset and Super Set
# A set can be a subset or super set of other sets:
#   Subset:     issubset()
#   Super set:  issuperset()

print(whole_numbers.issubset(even_numbers))  # False, because it is a super set
print(whole_numbers.issuperset(even_numbers))  # True
print(even_numbers.issubset(whole_numbers))  # True
print(python.issubset(dragon))     # False
print()

# Checking the Difference Between Two Sets
print(whole_numbers.difference(even_numbers))  # {1, 3, 5, 7, 9}
print(python.difference(dragon))  # {'p', 'y', 't'}
print(dragon.difference(python))  # {'d', 'r', 'a', 'g'}
print()

# Finding Symmetric Difference Between Two Sets
# It returns the the symmetric difference between two sets.
# It means that it returns a set that contains all items from both sets,
# except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))
print(python.symmetric_difference(dragon))
print()

# Joint or disjoint Sets
# If two Sets do not have a common item or items, we call them disjoint sets.
# We can check if two sets are joint or disjoint using the .isdisjoint() method.
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))  # True, there are no common items.
print(python.isdisjoint(dragon))  # False, because {'o', 'n'} are in both sets.
