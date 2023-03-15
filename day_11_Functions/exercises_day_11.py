from countries_data import countries_data
from math import sqrt
import statistics
from keyword import iskeyword

print("### Exercises: Day 11")

print()
print("## Exercises: Level 1")

print()
print("01. Declare a function add_two_numbers. It takes two parameters and it returns a sum.")


def add_two_numbers(a, b):
    return a + b


print()
print("""02. Area of a circle is calculated as follows: area = Pi x r x r. 
      Write a function that calculates area_of_circle.""")


def area_of_circle(r, Pi=3.14):
    return Pi * r * r


print()
print("""03. Write a function called add_all_nums which takes arbitrary number of
      arguments and sums all the arguments. 
      Check if all the list items are number types. If not do give a reasonable feedback.""")


def add_all_nums(*args):
    total = 0
    for i in args:
        if str(i).isdigit() == False:
            print("All arguments must be numbers")
            total = 0
            break
        else:
            total += i
    return total


print(add_all_nums(8, 2, "a"))

print()
print("""04. Temperature in Celsius can be converted to Fahrenheit using this formula: 
      F = (C x 9/5) + 32. 
      Write a function which converts C to F, convert_celsius_to_fahrenheit.""")


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


print(convert_celsius_to_fahrenheit(0))

print()
print("""05. Write a function called check-season, it takes a month parameter and returns 
      the season: Autumn, Winter, Spring or Summer.""")


def check_season(month):
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    elif month in ["September", "October", "November"]:
        return "Autumn"
    else:
        return "Not a valid month name"


print(check_season("March"))

print()
print("06. Write a function called calculate_slope which return the slope of a linear equation")


def calculate_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


print()
print("""07. Quadratic equation is calculated as follows: ax^2 + bx + c = 0. 
      Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.""")


def solve_quadratic_eqn(a, b, c):
    print(f"For Quadratic Formula: {a}*x^2 + {b}x + {c} = 0")
    # 'a' must be bigger than 0, otherwise won't be not valid.
    if a > 0:
        # if 'b' is between -6 and +6, result will be a complex root.
        if b >= 6 or b <= -6:
            x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
            x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
            y1 = (a*(x1**2)) + (b*x1) + c
            y2 = (a*(x2**2)) + (b*x2) + c
            if y1 == 0 and y2 == 0:
                print(f"'x' must be either '{x1}' or '{x2}' to equal 0.")
            elif y1 == 0:
                print(f"'x' must be '{x1}' to equal 0.")
            elif y2 == 0:
                print(f"'x' must be '{x2}' to equal 0.")
        else:
            print("If 'b' is between -6 and +6, result will be a complex root.")
    else:
        print("'a' must be bigger than 0, otherwise it will return an error.")


solve_quadratic_eqn(1, 6, 9)

print()
print("""08. Declare a function named print_list. 
      It takes a list as a parameter and it prints out each element of the list.""")


def print_list(list):
    for element in list:
        print(element)


print()
print("""09. Declare a function named reverse_list. 
      It takes an array as a parameter and it returns the reverse of the array (use loops).
        print(reverse_list([1, 2, 3, 4, 5]))
        # [5, 4, 3, 2, 1]
        print(reverse_list(["A", "B", "C"]))
        # ["C", "B", "A"]""")


def reverse_list(lista):
    reversed = list()
    length = len(lista)-1
    while length >= 0:
        reversed.append(lista[length])
        length -= 1
    return reversed


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

print()
print("""10. Declare a function named capitalize_list_items. 
      It takes a list as a parameter and it returns a capitalized list of items""")


def capitalize_list_items(lista):
    capitalized_list = []
    for item in lista:
        capitalized_list.append(str(item).capitalize())
    return capitalized_list


print(capitalize_list_items(["uno", "dos", "tres"]))

print()
print("""11. Declare a function named add_item. 
      It takes a list and an item parameters. 
      It returns a list with the item added at the end.
        food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
        print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
        numbers = [2, 3, 7, 9];
        print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]""")

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]


def add_item(lista, item):
    lista.append(item)
    return lista


print(add_item(food_staff, 'Meat'))
print(add_item(numbers, 5))

print()
print("""12. Declare a function named remove_item. 
      It takes a list and an item parameters. 
      It returns a list with the item removed from it.
        food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
        print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
        numbers = [2, 3, 7, 9];
        print(remove_item(numbers, 3))  # [2, 7, 9]""")


def remove_item(lista, item):
    lista.remove(item) if item in lista else lista
    return lista


print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))

print()
print("""13. Declare a function named sum_of_numbers. 
      It takes a number parameter and it adds all the numbers in that range.
        print(sum_of_numbers(5))  # 15
        print(sum_all_numbers(10))  # 55
        print(sum_all_numbers(100))  # 5050""")


def sum_of_numbers(number):
    total = 0
    for i in range(number+1):
        total += i
    return total


print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

print()
print("""14. Declare a function named sum_of_odds. 
      It takes a number parameter and it adds all the odd numbers in that range.""")


def sum_of_odds(number):
    total = 0
    for i in range(number+1):
        if i % 2 != 0:
            total += i
    return total


print(sum_of_odds(10))

print()
print("""15. Declare a function named sum_of_even. 
      It takes a number parameter and it adds all the even numbers in that range.""")


def sum_of_evens(number):
    total = 0
    for i in range(number+1):
        if i % 2 == 0:
            total += i
    return total


print(sum_of_evens(10))

print()
print()
print("## Exercises: Level 2")

print()
print("""01. Declare a function named evens_and_odds. 
      It takes a positive integer as parameter and it counts number of evens and odds in the number.
        print(evens_and_odds(100))
        # The number of odds are 50.
        # The number of evens are 51.""")


def evens_and_odds(number):
    evens = 0
    odds = 0
    for i in range(number+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"""
The number of odds are {odds}
The number of evens are {evens}""")


evens_and_odds(100)

print()
print("""02. Call your function factorial. 
      It takes a whole number as a parameter and it return a factorial of the number""")


def factorial(number):
    total = 1
    for i in range(number):
        total *= i+1
    print(f"{total} is {number}!")


factorial(5)

print()
print("""03. Call your function is_empty.
      It takes a parameter and it checks if it is empty or not""")


def is_empty(arg):
    return True if len(arg) == 0 else False


print(is_empty(""))

print()
print("""04. Write different functions which take lists. 
      They should calculate_mean, calculate_median, calculate_mode, 
      calculate_range, calculate_variance, calculate_std (standard deviation).""")


def calculate_mean(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)


print("calculate_mean")
print(calculate_mean([7, 5, 0, 7, 8, 5, 5, 4, 1, 5]))


def calculate_median(lista):
    lista.sort()
    length = len(lista)
    median = 0
    if length % 2 != 0:
        length += 1
    index = int((length / 2) - 1)
    median = lista[index]
    return median


print("calculate_median")
print(calculate_median([26.1, 25.6, 25.7, 25.2, 25.0, 27.8, 24.1]))


def calculate_mode(lista):
    lista_dict = dict()
    for item in lista:
        lista_dict[item] = lista.count(item)

    lista_dict_sorted = sorted(
        lista_dict.items(), key=lambda x: x[1], reverse=True)
    mode = lista_dict_sorted[0][0]
    return mode


print("calculate_mode")
print(calculate_mode([7, 5, 0, 7, 8, 5, 5, 7, 4, 1, 5, 7]))


def calc_mode(lista):
    return statistics.multimode(lista)


print(calc_mode([7, 5, 0, 7, 8, 5, 5, 7, 4, 1, 5, 7]))
print(calc_mode(["few", "few", "many", "some", "many"]))
print(calc_mode([1, 2, 3]))


def calculate_range(lista):
    lista.sort()
    a = lista[0]
    b = lista[-1]
    return b-a


print("calculate_range")
print(calculate_range([1, 6, 3, 9]))


def calculate_variance(lista):
    mean = calculate_mean(lista)
    sqrd_difference = []
    for i in lista:
        calc = (i-mean)**2
        sqrd_difference.append(calc)
    variance = calculate_mean(sqrd_difference)
    return variance


print("calculate_variance")
print(calculate_variance([600, 470, 170, 430, 300]))


def calculate_stdev(lista):
    stdev = sqrt(calculate_variance(lista))
    return stdev


print("calculate_stdev")
print(calculate_stdev([600, 470, 170, 430, 300]))

print()
print()
print("## Exercises: Level 3")

print()
print("01. Write a function called is_prime, which checks if a number is prime.")


def is_prime(number):
    # Check if the number is less than or equal to 1, return False if it is
    if number <= 1:
        return False
    # Loop through all numbers from 2 to the square root of n (rounded down to the nearest integer)
    for i in range(2, int(number**0.5)+1):
        # If number is divisible by any of these numbers, return False
        if number % i == 0:
            return False
    # If n is not divisible by any of these numbers, return True
    return True


print(is_prime(23))


print()
print("02. Write a functions which checks if all items are unique in the list.")


def is_unique(lista):
    for i in lista:
        if lista.count(i) > 1:
            return False
    return True


print(is_unique(['banana', 'orange', "mango", "lemon"]))
print(is_unique(['banana', 'orange', "mango", "lemon", "banana"]))

print()
print("03. Write a function which checks if all the items of the list are of the same data type.")


def is_same_type(lista):
    type_dict = dict()
    for i in lista:
        type_dict[type(i)] = 1
    return False if len(type_dict) > 1 else True


print(is_same_type(["banana", "2", "Hola mundo"]))
print(is_same_type(["banana", 2]))

print()
print("04. Write a function which check if provided variable is a valid python variable")
print()
print("from keyword import iskeyword")


def is_valid(name):
    return name.isidentifier() and not iskeyword(name)


print(is_valid('2'))
print(is_valid('name'))
print(is_valid('del'))
print(is_valid('last_name'))

print()
print("""05. Go to the data folder and access the countries-data.py file.
        Create a function called the most_spoken_languages in the world. 
            It should return 10 or 20 most spoken languages in the world in descending order
        Create a function called the most_populated_countries. 
            It should return 10 or 20 most populated countries in descending order.""")

print()
print("""from countries_data import countries_data""")
print()


def most_spoken_languages():
    lang_dict = dict()
    for country in countries_data:
        if "languages" in country:
            for language in country["languages"]:
                if language in lang_dict:
                    lang_dict[language] += 1
                else:
                    lang_dict[language] = 1
    spoken_lang_sort = sorted(
        lang_dict.items(), key=lambda x: x[1], reverse=True)
    print("The top most spoken languages are:")
    for i in range(15):
        print(spoken_lang_sort[i][0])


def most_populated_countries():
    pop_dict = dict()
    for country in countries_data:
        pop_dict[country["name"]] = country["population"]
    pop_sorted = sorted(pop_dict.items(), key=lambda x: x[1], reverse=True)
    print("The top most populated countries are:")
    for i in range(15):
        print(pop_sorted[i][0])


most_spoken_languages()
print()
most_populated_countries()
