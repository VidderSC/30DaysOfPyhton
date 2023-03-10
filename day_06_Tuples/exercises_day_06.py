# Exercises: Day 6
# - Exercises: Level 1

# 01. Create an empty tuple
brothers = tuple()
sisters = ()
# 02. Create a tuple containing names of your sisters and
# your brothers (imaginary siblings are fine):
brothers = ("Hermano1", "Hermano2")
sisters = ("Hermana1", "Hermana2")
print(brothers)
print(sisters)

# 03. Join brothers and sisters tuples and assign it to siblings:
siblings = brothers + sisters
print(siblings)

# 04. How many siblings do you have?
print(f"I have {len(siblings)} siblings.")

# 05. Modify the siblings tuple and add the name of your father and mother
# and assign it to family_members:
family_members = siblings + ("Father", "Mother")
print(family_members)
print()
# - Exercises: Level 2

# 01. Unpack siblings and parents from family_members
brother1, brother2, sister1, sister2, father, mother = family_members
print(brother1)
print(brother2)
print(sister1)
print(sister2)
print(father)
print(mother)
print()
# another way
brother1, brother2, sister1, sister2 = family_members[:4]
father, mother = family_members[-2:]
print(brother1)
print(brother2)
print(sister1)
print(sister2)
print(father)
print(mother)
print()

# 02. Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animals = ("Fish", "Pork", "Beef", "Chicken")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
print()

# 03. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 04. Slice out the middle item or items from the food_stuff_tp tuple
# or food_stuff_lt list.
length = len(food_stuff_tp) - 1
middle = length // 2
if length % 2 == 0:
    print(food_stuff_tp[middle:middle+2])
else:
    print(food_stuff_tp[middle:middle+1])
print()

# 05. Slice out the first three items and the last three items
# from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

# 06. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 07. Check if an item exists in tuple:
#       Check if 'Estonia' is a nordic country
#       Check if 'Iceland' is a nordic country
#
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
