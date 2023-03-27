"""
Exercises: Day 18
"""
import re
from collections import Counter
from pprint import pprint
import string

print("# Exercises: Level 1")
print()
print("1. What is the most frequent word in the following paragraph?")
PARAGRAPH = """I love teaching. If you do not love teaching what else can you love. \
I love Python if you do not love something which can give you all the capabilities \
to develop an application what else can you love."""
print(PARAGRAPH)


def count_words(text):
    """We use this function to count the words that are in the passes text."""

    no_dots = re.sub(r"[.]", "", text)
    splitted_text = re.split(" ", no_dots)
    count = Counter(splitted_text).most_common()
    return count


pprint(count_words(PARAGRAPH))

print()
TEXTO = """The position of some particles on the horizontal x-axis are \
-12, -4, -3 and -1 in the negative direction, 0 at origin, 8 and 4 in the \
positive direction."""
print(TEXTO)

print("""
2. Extract the numbers from the previous text and find the distance between the two furthest particles.
""")

points = re.findall(r"-?\d{1,2}", TEXTO)
print(points)
sorted_points = sorted([int(point) for point in points])
distance = sorted_points[-1] - sorted_points[0]
print(distance)

print()
print("# Exercises: Level 2")
print()
print("1. Write a pattern which identifies if a string is a valid python variable")


def is_valid_variable(variable):
    """ Rules for Python variables:
    - Must start with a letter or the underscore character
    - Cannot start with a number
    - Can only contain (A-z, 0-9, and _ )"""
    return not bool(re.search(r"^\s|^\d|-", variable))


print(f"' first_name': {is_valid_variable(' first_name')}")
print(f"'first_name': {is_valid_variable('first_name')}")
print(f"'first-name': {is_valid_variable('first-name')}")
print(f"'1first_name': {is_valid_variable('1first_name')}")
print(f"'firstname': {is_valid_variable('firstname')}")


print()
print("# Exercises: Level 3")
print()
print("1. Clean the following text. After cleaning, count three most frequent words in the string.")
SENTENCE = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re \
rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n \
any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
print(SENTENCE)
print()


def clean_text(text):
    """Clean the text"""
    return re.sub(rf"[{string.punctuation}]*", "", text)


print(clean_text(SENTENCE))


def count_clean_words(text):
    """We use this function to count the words that are in the passes text."""
    splitted_text = re.split(" ", clean_text(text))
    count = Counter(splitted_text).most_common()
    return count


def most_frequent_words(text):
    """We find the top 3 most frequent words in the cleaned text"""
    top_list = []
    all_cleaned_text = dict(count_clean_words(text))
    cleaned_text_sorted = sorted(
        all_cleaned_text.items(), key=lambda x: x[1], reverse=True)
    index = 0
    while index < 3:
        top_list.append(cleaned_text_sorted[index])
        index += 1
    return top_list


pprint(most_frequent_words(SENTENCE))
