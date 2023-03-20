from countries_data import countries_data
from countries import countries as countries2
from functools import reduce

# Exercises: Day 14
countries = ['Estonia', 'Finland', 'Sweden',
             'Denmark', 'Norway', 'Iceland', 'Spain']
names = ['Vidders', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

print("""# 01. Explain the difference between map, filter, and reduce:

All of them takes a function and an iterable as parameters,
but the function passed to filter() must return a boolean value.
- map() returns an iterable.
- filter() returns a filtered iterable following the passed function criteria.
- reduce() returns a value, not an iterable
""")

print("""# 02. Explain the difference between higher order function, closure and decorator:

- Higher Order Function (HOF) is called to a function that can take another function as
    a parameter and/or that can return a function.
- Closure is known for allowing to access the outer scope of an enclosing function, when
    nesting functions. To creater a closure we need to return the inner function.
- Decorator is to provide new functionality to an existing object without
    modifying its structure. To create a decorator, we need an outer function and
    an inner wrapper function.
""")

# 03. Define a call function before map, filter or reduce, see examples.


def square(num):
    return num * num


def uppercase(str):
    return str.upper()


def find_land(str):
    return "land" not in str


def add_two_nums(x, y):
    return x + y


# 04. Use for loop to print each country in the countries list.

for country in countries:
    print(country)

print()
# 05. Use for to print each name in the names list.

for name in names:
    print(name)

print()
# 06. Use for to print each number in the numbers list.
for number in numbers:
    print(number)

print()
# Exercises: Level 2

# 01. Use map to create a new list by changing each country to
# uppercase in the countries list

countries_upper = map(uppercase, countries)
print(list(countries_upper))

# 02. Use map to create a new list by changing each number to
# its square in the numbers list

numbers_squared = map(square, numbers)
print(list(numbers_squared))


# 03. Use map to change each name to uppercase in the names list

names_upper = map(lambda x: x.upper(), names)
print(list(names_upper))

# 04. Use filter to filter out countries containing 'land'.

countries_no_land = filter(find_land, countries)
print(list(countries_no_land))


# 05. Use filter to filter out countries having exactly six characters.

countries_six = filter(lambda x: len(x) == 6, countries)
print(list(countries_six))

# 06. Use filter to filter out countries containing six letters and
# more in the country list.

countries_six_or_less = filter(lambda x: len(x) < 6, countries)
print(list(countries_six_or_less))

# 07. Use filter to filter out countries starting with an 'E'

countries_no_start_e = filter(lambda x: "E" not in x[0], countries)
print(list(countries_no_start_e))

print()
# 08. Chain two or more list iterators
# (eg. arr.map(callback).filter(callback).reduce(callback))

chained = map(uppercase, filter(find_land, countries))
print(list(chained))

print()
# 09. Declare a function called get_string_lists which takes a list
# as a parameter and then returns a list containing only string items.


def get_string_lists(lst):
    return [string for string in lst if type(string) is str]


print(get_string_lists(
    [5, "Only", True, "Strings", False, 8, "are", "returned"]))

print()
# 10. Use reduce to sum all the numbers in the numbers list.
print(reduce(add_two_nums, numbers))

print()
# 11. Use reduce to concatenate all the countries and to produce this
# sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are
# north European countries


def combine_countries(a, b):
    if b == "Spain":
        return a + " and " + b
    else:
        return a + ", " + b


print(reduce(combine_countries, countries) + " are European countries")

print()
# 12. Declare a function called categorize_countries that returns a
# list of countries with some common pattern
# (you can find the countries list in this repository as countries.py
# (eg 'land', 'ia', 'island', 'stan')).


def categorize_countries(string):
    return [country for country in countries2 if string in country]


print(list(categorize_countries("land")))

print()
print(list(categorize_countries("ia")))

print()
print(list(categorize_countries("Island")))

print()
print(list(categorize_countries("stan")))

print()
print(list(categorize_countries("ain")))

print()
# 13. Create a function returning a dictionary, where keys stand for
# starting letters of countries and values are the number of
# country names starting with that letter.


def countries_initials_dict():
    start_letter = []
    set_start_letter = set()
    dct = {}
    for country in countries2:
        start_letter.append(country[0])
    set_start_letter = set(start_letter)
    for key in set_start_letter:
        dct[key] = start_letter.count(key)
    return dct


print(countries_initials_dict())

print()
# 14. Declare a get_first_ten_countries function -
# it returns a list of first ten countries from the countries.py list in the data folder.


def get_first_ten_countries():
    lst = []
    for i in range(0, 10):
        lst.append(countries2[i])
    return lst


print(list(get_first_ten_countries()))

# 15. Declare a get_last_ten_countries function that returns the
# last ten countries in the countries list.


def get_last_ten_countries():
    lst = []
    for i in range(-10, 0):
        lst.append(countries2[i])
    return lst


print(list(get_last_ten_countries()))

print()
# Exercises: Level 3 - (Use the countries_data.py file)

print("# 01. Sort countries by name, by capital, by population")


def sort_countries(string, rev=False):
    if string == "population":
        pop_dict = dict()
        for country in countries_data:
            pop_dict[country["name"]] = country["population"]
        pop_sorted = sorted(pop_dict.items(), key=lambda x: x[1], reverse=rev)
        ps = [pop[0] for pop in pop_sorted]
        return ps
    elif string == "language":
        language_dict = dict()
        for country in countries_data:
            if "languages" in country:
                for language in country["languages"]:
                    if language in language_dict:
                        language_dict[language] += 1
                    else:
                        language_dict[language] = 1
        spoken_languages_sorted = sorted(
            language_dict.items(), key=lambda x: x[1], reverse=rev)
        sls = [lan[0] for lan in spoken_languages_sorted]
        return sls
    else:
        countries_lst = []
        for country in countries_data:
            countries_lst.append(country[string])
        countries_lst.sort(reverse=rev)
        return countries_lst


print("List of countries sorted by Name:")
print(list(sort_countries("name")))

print()
print("List of countries sorted by Capital:")
print(list(sort_countries("capital")))

print()
print("List of countries sorted by Population:")
print(list(sort_countries("population")))

print()
print("# 02. Sort out the ten most spoken languages by location.")


def get_first_ten(lista):
    lst = []
    for i in range(0, 10):
        lst.append(lista[i])
    return lst


print(list(get_first_ten(sort_countries("language", True))))

print()
print("# 03. Sort out the ten most populated countries.")

print(list(get_first_ten(sort_countries("population", True))))
