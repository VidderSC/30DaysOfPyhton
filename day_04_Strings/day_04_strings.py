# Day 4 - 30DaysOfPython Challenge

# Strings
letter = 'P'  # A string could be a single character or a bunch of text
print(letter)  # P
print(len(letter))  # 1
print(type(letter))  # <class 'str'>
greeting = "Hello, World!"  # String could be made using single or double quotes
print(greeting)             # Hello, World!
print(len(greeting))        # 13
print()

# Multiline string is created by using triple quotes.
multiline = """ This is an example of
 a multiline string that consists of
 three lines."""
print(multiline)
print()
multiline = '''This is the same example of
 a multiline string that consists of three
 lines but created with single quotes.'''
print(multiline)
print()

# String concatenation
first_name = 'Vidders'
last_name = "SC"
space = " "
full_name = first_name + space + last_name
full_name2 = first_name + " " + last_name
print(full_name)
print(full_name2)
print()

# Escape sequences in Strings
# In Python and in other languages \ followed by a character is an escape sequence.
"""
\n = new line or line break
\t = Insert Tab [4 spaces]
\\ = Back slash \
\' = Single quote (')
\" = Double quotes (")
"""
print("I hope you are enjoying this challenge.\nAre you?")  # line break
print("Days\tTopics\tExercises")  # add tabs
print("Day 1\t  3\t\t\t3")
print("Day 2\t  4\t\t\t5")
print("Day 3\t  2\t\t\t26")
print("Day 4\t  1\t\t\t30")
print("This is a backslash simbol \\, a single quote \' and a double quote \"")
print()

# String Formatting
"""
Old Style String Formatting (% Operator)
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Float number with fixed precision - %.2f
"""
language = "Python"
old_style_formatting = "I am %s %s, I\'m learning %s and how to use the old style formatting." % (
    first_name, last_name, language)
print(old_style_formatting)
radius = 10
PI = 3.14
area = PI * radius ** 2
old_style_formatting2 = 'The area of a circle with radius %d is %.2f.' % (
    radius, area)
print(old_style_formatting2)
print()

# New Style String Formatting (Since version 3)
new_style_formatting = "I am {} {} and I'm learning {} and how to use the new style formatting.".format(
    first_name, last_name, language)
print(new_style_formatting)

a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
# Limits it to three digits after decimal
print("{} + {} = {:.3f}".format(a, b, a / b))
new_style_formatting2 = 'The area of a circle with radius {} is {:.2f}.'.format(
    radius, area)
print(new_style_formatting2)

# Newest Style formating (Since version 3.6)
# String Interpolation

print(f'{a} + {b} = {a + b}')
print(f"{a} / {b} = {a / b:.2f}")
print(f'The area of a circle with radius {radius} is {area:.2f}.')
print()

# Unpacking Characters
idioma = "Español"
# You can access the characters by the index.
c0, c1, c2, c3, c4, c5, c6 = idioma
# To unpack you need as many variables as characters in the word or sentence.
print(c0)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print()

fist_letter = idioma[0]
print(fist_letter)
second_letter = idioma[1]
print(second_letter)
print()
# Negative indexing. We use it to start from the right.

last_letter = idioma[-1]
second_last_letter = idioma[-2]
print(last_letter)
print(second_last_letter)
print()

# Slicing Strings
first_three = idioma[0:3]
print(first_three)
middle_three = idioma[2:5]
print(middle_three)
last_three = idioma[-3:]
print(last_three)
print()

# Reversing string
greeting = "Hello, World!"
print(greeting[::-1])
print()

# Skipping Characters
skip_every_second = idioma[0:7:2]
print(skip_every_second)
print()

# String Methods

challenge = "thirty days of python"
print(challenge.capitalize())  # Converts the First character in capital letter
print(challenge.count("y"))  # Counts how many 'y' characters are in challenge
# Counts how many 'th' characters are in challenge
print(challenge.count("th"))
# Counts 'y' characters from indexes 7 to 14
print(challenge.count("y", 7, 14))
print(challenge.endswith('on'))  # Checks the ending and returns Boolean.
print(challenge.endswith('tion'))
print()

# expandtabs() Replaces tab character with spaces, default tab size is 8.
# It takes tab size argument
challenge = "thirty\tdays\tof\tpython"
print(challenge)
print(challenge.expandtabs())
print(challenge.expandtabs(10))
print()

challenge = "thirty days of python"
# Returns the index of the first 'y' character found, -1 if not found.
print(challenge.find('y'))
print(challenge.find('th'))
# Returns the index of the last 'y' character found, -1 if not found.
print(challenge.rfind('y'))
print(challenge.rfind('th'))
print()

# index(): Returns the lowest index of a substring, additional arguments
# indicate starting and ending index (default 0 and string length - 1).
# If the substring is not found it raises a valueError.
sub_string = 'th'
print(challenge.index(sub_string))
# print(challenge.index(sub_string, 9))  # Returns valueError
# rindex(): Returns the highest index of a substring, additional arguments
# indicate starting and ending index (default 0 and string length - 1)
print(challenge.rindex(sub_string))
print()

# isalnum(): Checks alphanumeric character
# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
# isdecimal(): Checks if all characters in a string are decimal (0-9)
# isnumeric(): Checks if all characters in a string are numbers or number related,
# just like isdigit(), but accepts more symbols, like ½
# isdigit(): Checks if all characters in a string are numbers
# (0-9 and some other unicode characters for numbers)
# isidentifier(): Checks for a valid identifier - it checks if a string 
# is a valid variable name
# islower(): Checks if all alphabet characters in the string are lowercase
# isupper(): Checks if all alphabet characters in the string are uppercase

challenge = "ThirtyDaysPython"
print(challenge.isalnum())  # True
print(challenge.isalpha())  # True
print(challenge.isdecimal())  # False
challenge = "30DaysPython"
print(challenge.isalnum())  # True
print(challenge.isalpha())  # False, numbers are NOT alphabet.
challenge = "Thirty days of python"
print(challenge.isalnum())  # False, space is NOT alphanumeric.
print(challenge.isalpha())  # False, space is NOT alphabet.
challenge = "30 days of python"
print(challenge.isalnum())  # False

# join(): Returns a concatenated string
# strip(): Removes all given characters starting from the beginning 
# and end of the string
# replace(): Replaces substring with a given string
# split(): Splits the string, using given string or space as a separator

# title(): Returns a title cased string
# swapcase(): Converts all uppercase characters to lowercase and 
# all lowercase characters to uppercase characters

# startswith(): Checks if String Starts with the Specified String
