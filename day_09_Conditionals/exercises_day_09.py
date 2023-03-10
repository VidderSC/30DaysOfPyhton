# Exercises: Day 9

# Exercises: Level 1

# 01. Get user input using input(“Enter your age: ”).
# If user is 18 or older, give feedback:
# You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.
# Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input('Enter your age: '))
diff = 18 - age
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    if diff > 1:
        print(f"You need {diff} more years to learn to drive.")
    else:
        print(f"You need 1 more year to learn to drive.")
print()

# 02. Compare the values of my_age and your_age using if … else.
# Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age.
# Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 43
print("Who is older (you or me)?")
your_age = int(input(f"Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    if diff > 1:
        print(f"You are {diff} years older than me.")
    else:
        print(f"You are 1 year older than me.")
elif your_age == my_age:
    print("We are both the same age!")
else:
    diff = my_age - your_age
    if diff > 1:
        print(f"I am {diff} years older than you.")
    else:
        print(f"I am 1 year older than you.")
print()

# 03. Get two numbers from the user using input prompt.
# If a is greater than b return: a is greater than b,
# if a is less b return: a is smaller than b,
# else return: a is equal to b.
# Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
if a > b:
    print("A is greater than B")
elif a < b:
    print("B is greater than A")
else:
    print("A is equal to B")
print()


# Exercises: Level 2

# 01. Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input("Enter your score (0-100): "))
if 90 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
else:
    print("F")
print()

# 02. Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is:
# September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring
# June, July or August, the season is Summer
autumn = {"September", "October", "November"}
winter = {"December", "January", "February"}
spring = {"March", "April", "May"}
summer = {"June", "July", "August"}
month = input("Enter the month: ")
if month in spring:
    print("The season is Spring")
elif month in summer:
    print("The season is Summer")
elif month in autumn:
    print("The season is Autumn")
elif month in winter:
    print("The season is Winter")
else:
    print("You didn't enter a correct month")
print()

# 03. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and
# print the modified list.
# If the fruit exists print('That fruit already exist in the list')
print(fruits)
print()
fruit = input("Enter a fruit in lower case: ")
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
print()


# Exercises: Level 3

# 01. Here we have a person dictionary.
person = {
    'first_name': 'Vidders',
    'last_name': 'SC',
    'age': 69,
    'country': 'Spain',
    'is_married': True,
    'skills': ['Java', 'HTML', 'CSS', 'MySQL', 'Python'],
    # 'skills': ["JavaScript", "React"],
    # 'skills': ["JavaScript", "React", "Node", "Python", "MongoDB"],
    # 'skills': ["Java", "Node", "Python", "MongoDB"],
    'address': {
        'street': 'Beverly Hills',
        'zipcode': '90210'
    }
}
print(person)
print()

# A. Check if the person dictionary has skills key,
# if so print out the middle skill in the skills list.
if "skills" in person:
    length = len(person["skills"])
    print(f'Middle Skill: {person["skills"][length//2]}')

# B. Check if the person dictionary has skills key,
# if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    print(f"Knows Python? {'Python' in person['skills']}")

# C. If a person skills has only JavaScript and React,
# print('He is a front end developer'),
# if the person skills has Node, Python, MongoDB,
# print('He is a backend developer'),
# if the person skills has React, Node and MongoDB,
# print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results
# more conditions can be nested!
person_lst = list(person.values())
skills = set(person_lst[5])
print(skills)

front_end = {"JavaScript", "React"}
back_end = {"Node", "Python", "MongoDB"}
full_stack = {"React", "Node", "MongoDB"}
learning = {"Python", "Java"}
skills_len = len(skills)

if skills_len == 2:
    if skills.intersection(front_end) == front_end:
        print('He is a front end developer')
else:
    if skills.intersection(full_stack) == full_stack:
        print('He is a fullstack developer')
    elif skills.intersection(back_end) == back_end:
        print('He is a backend developer')
    elif skills.intersection(learning) == learning:
        print("He is learning to become a developer")
    else:
        print("unkown title")
print()

# D. If the person is married and if he lives in Spain,
# print the information in the following format:
# {fist_name} {last_name} lives in {country}. He is married.
if person['is_married'] and person['country'] == "Spain":
    print(
        f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married.')
