# Day 18 - 30DaysOfPython Challenge

# Regular Expressions
"""
A regular expression or RegEx is a special text string that helps to 
find patterns in data. A RegEx can be used to check if some pattern 
exists in a different data type. 

To use RegEx in python first we should import the RegEx module 're':
'import re'
After importing the module we can use it to detect or find patterns.

Methods in 're' Module:
To find a pattern we use different set of re character sets that allows
to search for a match in a string:

- re.match(): Searches only in the beginning of the first line of the 
        string and returns matched objects if found, else returns None.
- re.search: Returns a match object if there is one anywhere in the 
        string, including multiline strings.
- re.findall: Returns a list containing all matches.
- re.split: Takes a string, splits it at the match points, returns a list.
- re.sub: Replaces one or many matches within a string.

# Match 
Syntax: 're.match(substring, string, re.I)'
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
"""

import re

TXT = "I'm learning Python"

# It returns an object with span, and match
match1 = re.match("I'm learning", TXT, re.I)

print(match1)  # <re.Match object; span=(0, 12), match="I'm learning">

# We can get the starting and ending position of the match as tuple using span
span1 = match1.span()
print(span1)  # (0, 12)

# Lets find the start and stop position from the span
start, end = span1
print(start, end)  # 0 12

substring = TXT[start:end]
print(substring)  # I'm learning

# As you can see from the example above, the pattern or substring that we are
# looking for is 'I'm learning'. The match function returns an object ONLY if
# the text starts with the said pattern.
print()

match2 = re.match("I learn", TXT, re.I)
print(match2)  # None

# Search

TXT1 = '''Python is the most beautiful language that
a human being has ever created.
I recommend python for a first programming language'''

match3 = re.search("first", TXT1, re.I)
print(match3)

span2 = match3.span()
print(span2)

start2, end2 = span2
substring = TXT1[start2:end2]
print(substring)

# Search is better than Match because it can look for the pattern or substring
# thougout the text. And return the first positive match found, otherwise will
# return None.

# Findall: This function will return a list of all matches.

print()
matches = re.findall("language", TXT1, re.I)
print(matches)  # ['language', 'language']

matches1 = re.findall("python", TXT1, re.I)
print(matches1)  # ['Python', 'python']

# Without re.I (not case sensitive), will only find the exact match.
matches2 = re.findall("python", TXT1)
print(matches2)  # ['python']

# Unless we change the format of our pattern to get the same result.
matches3 = re.findall("[Pp]ython", TXT1)
print(matches3)  # ['Python', 'python']

matches4 = re.findall("Python|python", TXT1)
print(matches4)  # ['Python', 'python']

# Replacing a substring
TEXT = '''Python is the most beautiful language
that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub("Python|python", "JS", TEXT)
print(match_replaced)

print()
match_replaced = re.sub("[Pp]ython", "JS", TEXT)
print(match_replaced)

print()
# As we can see, re.I doesn't work with sub.
match_replaced = re.sub("python", "JS", TEXT, re.I)
print(match_replaced)

print()
TXT2 = "%I a%m le%%a%%rn%%i%ng P%y%t%%h%%on%% %%a%n%%d I%'%m m%%o%t%%iv%%a%t%%ed%%.%%"
cleaned = re.sub("%", "", TXT2)
print(cleaned)

# Splitting text using RegEx (re) Split

print(re.split("\n", TEXT))  # Split text on every end of line symbol.
print()

# Writting RegEx Patterns

RE_PATTERN = r"apple"
RE_PATTERN2 = r"[Aa]pple"

NEW_TEXT = """Apple and banana are fruits. And an old cliche says:
An apple a day keeps the doctor away.
And we are replacing it for:
A banana a day keeps the doctor far far away"""

all_matches = re.findall(RE_PATTERN, NEW_TEXT)
print(all_matches)

all_matches2 = re.findall(RE_PATTERN, NEW_TEXT, re.I)
print(all_matches2)

all_matches3 = re.findall(RE_PATTERN2, NEW_TEXT, re.I)
print(all_matches3)
print()

# Syntax for patterns:

# []: A set of characters
# -- [a-c] means, a or b or c
# -- [a-z] means, any letter from a to z
# -- [A-Z] means, any character from A to Z
# -- [0-3] means, 0 or 1 or 2 or 3
# -- [0-9] means any number from 0 to 9
# -- [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
# -- \d means: match where the string contains digits (numbers from 0-9)
# -- \D means: match where the string does not contain digits
# . : any character except new line character(\n)
# ^: starts with
# -- r'^substring' eg r'^love', a sentence that starts with a word love
# -- r'[^abc] means not a, not b, not c.
# $: ends with
# -- r'substring$' eg r'love$', sentence that ends with a word love
# *: zero or more times
# -- r'[a]*' means a optional or it can occur many times.
# +: one or more times
# -- r'[a]+' means at least once (or more)
# ?: zero or one time
# -- r'[a]?' means zero times or once
# {3}: Exactly 3 characters
# {3,}: At least 3 characters
# {3,8}: 3 to 8 characters
# |: Either or
# -- r'apple|banana' means either apple or a banana
# (): Capture and group

# Examples:

REGEX_PATTERN = r"[Aa]pple|[Bb]anana"
matches5 = re.findall(REGEX_PATTERN, NEW_TEXT)
print(matches5)
print()

# Escape character (\)
OTHER_TEXT = "This regular expresion example was made on December 6,\
 2019 and revised on March 27, 2023"

REGEX_PATTERN1 = r"\d"  # d is a special character that means digits
matches6 = re.findall(REGEX_PATTERN1, OTHER_TEXT)
print(matches6)
print()

REGEX_PATTERN2 = r"\d+"  # + means one or more times
matches7 = re.findall(REGEX_PATTERN2, OTHER_TEXT)
print(matches7)
print()

# Period (.)
TEXT2 = "Apple and bananas are fruits"

# this square bracket means a and . means any character except new line.
REGEX_PATTERN3 = r"[a]."
matchs = re.findall(REGEX_PATTERN3, TEXT2)
print(matchs)

REGEX_PATTERN4 = r"[a].+"  # + means one or more times
matchs1 = re.findall(REGEX_PATTERN4, TEXT2)
print(matchs1)
print()

# Zero or more times (*)
# The pattern might not occur or it could occur many times.

REGEX_PATTERN5 = r"[a].*"
matchs2 = re.findall(REGEX_PATTERN5, TEXT2)
print(matchs2)
print()

# Zero or one time (?)
# The pattern might not occur or it could occur once.

TXT3 = '''I am not sure if there is a convention on how to write the
word e-mail. Some people write it as email others may write it 
as Email or E-mail.'''

RGX_PTTRN = r"[Ee]-?mail"  # ? means here that '-' is optional.

mtchs = re.findall(RGX_PTTRN, TXT3)
print(mtchs)
print()

# Quantifiers in RegEx
# We can specify the length of the substring we are looking for in a text
# using the curly brackets.

OTHER_TEXT = "This regular expresion example was made on December 6,\
 2019 and revised on March 27, 2023"

RGX_PTTRN1 = r"\d{4}"  # exactly 4 times
mtchs1 = re.findall(RGX_PTTRN1, OTHER_TEXT)
print(mtchs1)

RGX_PTTRN2 = r"\d{1,4}"  # from 1 to 4 times
mtchs2 = re.findall(RGX_PTTRN2, OTHER_TEXT)
print(mtchs2)
print()

# Cart ^
RGX_PTTRN3 = r"^This"  # ^ = Starts With
mtchs2 = re.findall(RGX_PTTRN3, OTHER_TEXT)
print(mtchs2)

# ^ in set character means negation. not 'A' to 'Z', not 'a' to 'z', no 'spaces'.
RGX_PTTRN4 = r"[^A-Za-z ]+"
mtchs3 = re.findall(RGX_PTTRN4, OTHER_TEXT)
print(mtchs3)
