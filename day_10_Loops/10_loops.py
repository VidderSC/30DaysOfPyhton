# Day 10 - 30DaysOfPython Challenge

# Loops
"""
In order to handle repetitive task programming languages use loops. 
Python provides the following two types of loops:
    While loop:
        We use the reserved word 'while' to make a while loop. 
        It is used to execute a block of statements repeatedly until 
        a given condition is satisfied. 
        When the condition becomes false, the lines of code after 
        the loop will be continued to be executed.
    For loop:
        A 'for' keyword is used to make a for loop, similar to other 
        programming languages, but with some syntax differences. 
        Loop is used for iterating over a sequence that is either a list, 
        a tuple, a dictionary, a set, or a string.
"""

print("# While loop")
count = 0
while count < 5:
    print(count)
    count = count + 1
# prints from 0 to 4
print()

print("""# If we are interested to run a block of code once the condition
# is no longer true, we can use 'else'.""")
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
print()

print("# Break and Continue - Part 1")
"""
Break:    We use break when we like to get out of or stop the loop.
Continue: With the continue statement we can skip the current 
          iteration, and continue with the next:
"""
print("# Break")
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# The above while loop only prints 0, 1, 2. When it reaches 3 will stop.
print()

print("# Continue")
count = 0
while count < 5:
    if count == 3:
        count += 1  # if we don't add this line, it'll become an infinite loop.
        continue
    print(count)
    count += 1
# The above while loop only prints 0, 1, 2 and 4, skipping the 3
print()

print()
print("# For Loops")
print()

print("# For loop with Lists")
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# 'num' is a temporary var to refer the items, valid only inside this loop
print()

print("# For loop with Strings")
language = 'Python'
for letter in language:
    print(letter)
print()

for i in range(len(language)):
    print(language[i])

# Both for loops above returns the same result
print()
print("# For loop with Tuples")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

print()

print("""# For loop with Dictionary:
  Looping through a dictionary gives you the keys of the dictionary.""")

person = {
    'first_name': 'Vidders',
    'last_name': 'SC',
    'age': 69,
    'country': 'Spain',
    'is_married': True,
    'skills': ['Java', 'HTML', 'CSS', 'MySQL', 'Python'],
    'address': {
        'street': 'Beverly Hills',
        'zipcode': '90210'
    }
}
for key in person:
    print(key)
print()

for key, value in person.items():
    # this way we get both keys and values printed out
    print(f"{key}: {value}")

print()
print("# For loop with Sets")
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

print()
print("Break and Continue - Part 2")
print()
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    # for short hand conditions need both if and else statements
    print('Next number should be ',
          number + 1) if number != 5 else print("loop's end")
print('outside the loop')

print()
print("# The Range Function")
"""
The range() function is used for a list of numbers. 
The range(start, end, step) takes three parameters:
    starting, ending and increment. 
By default it starts from 0 and the increment is 1. 
The range sequence needs at least 1 argument (end). 
"""
lst = list(range(11))
print("lst = list(range(11))")
print(lst)
print()

# 2 arguments indicate start and end of the sequence, step set to default 1
st = set(range(1, 11))
print("st = set(range(1, 11))  ")
print(st)
print()

lst = list(range(0, 11, 2))
print("lst = list(range(0,11,2))")
print(lst)
print()

st = set(range(0, 11, 2))
print("st = set(range(0,11,2))")
print(st)
print()

print()
print("# Nested For Loops")

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

print()
print("# For Else Loop")
print("  If we want to execute some message when the loop ends, we use else.")

last = 0
for num in range(11):
    print(num)   # prints 0 to 10, not including 11
    last = num
else:
    print(f'The loop stops at {last}')

print()
print("# Pass")
print("""In python when a statement is required (after semicolon ':'),
    but we don't like to execute any code there, 
    we can write the word pass to avoid errors. 
    Also we can use it as a placeholder, for future statements.
""")
for number in range(6):
    pass
