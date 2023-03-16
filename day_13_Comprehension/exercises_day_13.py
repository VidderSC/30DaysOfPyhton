print("## Exercises: Day 13 - Comprehension & Lambdas")

print()
print("01. Filter only negative and zero in the list using list comprehension")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_zero = [i for i in numbers if i <= 0]
print(neg_zero)

print()
print("02. Flatten the provided list of lists of lists to a one dimensional list")
list_of_lists = [
    [[1, 2, 3]],
    [[4, 5, 6]],
    [[7, 8, 9]]]

flatten = [number for row in list_of_lists for x in row for number in x]
print(flatten)

print()
print("03. Using list comprehension create the following list of tuples:")

fibbonazi = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(fibbonazi)


countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]]
print()
print(f"countries = {countries}")

print()
print("04. Flatten countries list to a new list all in capital letters:")

flatten_up = [country.upper()
              for row in countries for x in row for country in x]
print(flatten_up)

print()
print("05. Change countries to a list of dictionaries:")
country_dict_list = [{k: v} for row in countries for k, v in row]
print(country_dict_list)

print()
print("06. Change the following list of lists to a list of concatenated strings:")
names = [
    [('Stephen', 'Wozniak')],
    [('Steve', 'Jobs')],
    [('Bill', 'Gates')]
]
print(f"names = {names}")

concat_strings_list = "".join(
    [c for name in names for x in name for nm in x for c in nm])
print(concat_strings_list)


print()
print("""07. Write a lambda function which can solve 
    a slope or y-intercept of linear functions.
""")

# y = slope*x+b
# for function: y = 2x-2
# y = 2*0 - 2
# y = -2


x1, y1, x2, y2 = -2, -6, 2, 4

print("# Your IDE might change your 'lambdas' to 'def' because of PEP8.")
print("""PEP8: Always use a 'def' statement instead of an assignment statement that 
      binds a lambda expression directly to an identifier.
      """)
print("x1, y1, x2, y2 = -2, -6, 2, 4")
print()


print("# slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)")
def slope(x1, y1, x2, y2): return (y2-y1)/(x2-x1)


print(slope(x1, y1, x2, y2))


print("# y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1")
def y_intercept(x1, y1, x2, y2): return y1 - slope(x1, y1, x2, y2) * x1


print(y_intercept(x1, y1, x2, y2))
