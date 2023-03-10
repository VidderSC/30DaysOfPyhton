from countries import countries
from countries_data import countries_data

# Exercises: Day 10

# Exercises: Level 1
# 01. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)
print()

i = 0
while i <= 10:
    print(i)
    i += 1
print()

# 02. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)
print()

i = 10
while i >= 0:
    print(i)
    i -= 1
print()

# 03. Write a loop that makes seven calls to print(),
#     so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
for i in range(1, 8):
    print("#" * i)
print()

# 04. Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

for i in range(1, 9):
    for j in range(1, 10):
        # Using end=" " we indicate print to not end with a new line but with a space.
        print("#", end=" ")
    print()
print()

# 05. Print the following pattern:
#
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(11):
    print(f"{i} x {i} = {i*i}")
print()

# 06. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a
# for loop and print out the items.
for item in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(item)
print()

# 07. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print(i)
print()

# 08. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0, 101):
    print(i) if i % 2 != 0 else i
print()


# Exercises: Level 2

# 01. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for i in range(101):
    sum += i
print(f"The sum of all numbers is {sum}")
print()

# 02. Use for loop to iterate from 0 to 100 and print the sum of all evens and
# the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(
    f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}")
print()


# Exercises: Level 3

# 01. Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries containing the word land.
for country in countries:
    if country.find("land") != -1:
        print(country)
print()
# Another solution:
for country in countries:
    if ("land") in country:
        print(country)
print()

# 02. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
i = len(fruit_list)-1
while i >= 0:
    print(fruit_list[i])
    i -= 1
print()

# 03. Go to the data folder and use the countries_data.py file.
# 03.1. What are the total number of languages in the data
language_set = set()
for country in countries_data:
    if "languages" in country:
        for language in country["languages"]:
            language_set.add(language)
print(f"Total number of languages = {len(language_set)} languages.")
print()

# 03.2. Find the ten most spoken languages from the data
language_dict = dict()

for country in countries_data:
    if "languages" in country:
        for language in country["languages"]:
            if language in language_dict:
                language_dict[language] += 1
            else:
                language_dict[language] = 1

spoken_languages_sorted = sorted(
    language_dict.items(), key=lambda x: x[1], reverse=True)
print("The top 10 most spoken languages are:")
for i in range(10):
    print(spoken_languages_sorted[i][0])
print()

# 03.3. Find the 10 most populated countries in the world
pop_dict = dict()

for country in countries_data:
    pop_dict[country["name"]] = country["population"]

pop_sorted = sorted(pop_dict.items(), key=lambda x: x[1], reverse=True)
print("The top 10 most most populated countries are:")
for i in range(10):
    print(pop_sorted[i][0])
