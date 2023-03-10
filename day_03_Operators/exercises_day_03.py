# 01. Declare your age as integer variable
from math import sqrt
age = 43

# 02. Declare your height as a float variable
height = 1.75

# 03. Declare a variable that store a complex number
complex = 1 + 1j

# 04. Write a script that prompts the user to enter base and height
#     of the triangle and calculate an area of this triangle
#     (area = 0.5 x b x h).
#       Enter base: 20
#       Enter height: 10
#       The area of the triangle is 100
base = float(input('Enter the Base of the triangle: '))
height = float(input('Enter the Height of the triangle: '))
area = 0.5 * height * base
print('The Area of the triangle is', area)

# 05. Write a script that prompts the user to enter side a, side b,
#     and side c of the triangle. Calculate the perimeter of the triangle
#     (perimeter = a + b + c).
#       Enter side a: 5
#       Enter side b: 4
#       Enter side c: 3
#       The perimeter of the triangle is 12
side_a = float(input('Enter the side a: '))
side_b = float(input('Enter the side b: '))
side_c = float(input('Enter the side c: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is', perimeter)

# 06. Get length and width of a rectangle using prompt. Calculate:
#     Area (area = length x width)
#     Perimeter (perimeter = 2 x (length + width))
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width: '))
print(
    f'The area of the rectangle is {length * width} and the perimeter is {2 * (length + width)}.')

# 07. Get radius of a circle using prompt. Calculate:
#     Area (area = pi x r x r)
#     Circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius: "))
PI = 3.14
print(
    f"The area of the circle is {PI * radius ** 2} and it's circumference is {2 * PI * radius}.")
print()

# 08. Calculate the slope, x-intercept and y-intercept of y = 2x -2
intercept = (2 * 0) - 2
x1 = 1
y1 = (2 * x1) - 2
x2 = 2
y2 = (2 * x2) - 2
slope1 = (y2 - y1) / (x2 - x1)

print('x1 =', x1)
print('x2 =', x2)
print('y1 = (2 * x1) - 2 =', y1)
print('y2 = (2 * x2) - 2 =', y2)
print()
print('Slope1 ((y2 - y1) / (x2 - x1)) = ', slope1)
print('Intercept ((2 * 0) - 2) = ', intercept)
print()

# 09. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between
#     point (2, 2) and point (6,10)
print("""Slope is (m = y2-y1/x2-x1). 
    Find the slope and Euclidean distance between point (2, 2) and point (6,10)""")
x1, y1, x2, y2 = 2, 2, 6, 10


def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


slope2 = slope(x1, y1, x2, y2)
print("Slope2 = ", slope2)

print(f'Euclidean distance of ({x1},{y1}):', abs(x1-y1))
print(f'Euclidean distance of ({x2},{y2}):', abs(x2-y2))
print()

# 10. Compare the slopes in tasks 8 and 9.
print("slope1 == slope2 : ", slope1 == slope2)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values
#     and figure out at what x value y is going to be 0.

print("y = (x^2) + (6*x) + 9")
print()

for x in range(10):
    y = (x ** 2) + (6*x) + 9
    print(f'x = {x}')
    print(f'y = ({x**2} + {6*x} + 9) = {y}')
    print()

a = 1
b = 6
c = 9

if a > 0:  # 'a' must be bigger than 0, otherwise won't be not valid.
    if b % 2 == 0:
        # Logic for figuring out at what 'x' value 'y' is going to be '0'.
        # (ONLY when 'b' is even)
        # ax^2 + bx + c = 0
        # ax^2 + bx = -c
        # ax^2 + bx + (b/2)^2 = -c + (b/2)^2
        # rigth = -c + ((b/2)**2)
        # (ax + b/2)^2 = rigth
        # ax + b/2 = sqrt(rigth)
        # ax = sqrt(rigth) - (b/2)
        # x = (sqrt(rigth) - (b/2)) / a
        rigth = -c + ((b/2)**2)
        x = (sqrt(rigth) - (b/2)) / a
        print(f"'x' must be {x} for 'y' to be 0")
    else:
        # Logic for figuring out at what 'x' value 'y' is going to be '0'.
        # (This one works for any, but I wanted to use both ways.)
        # Quadratic equation: ax**2 + bx + c = 0
        print("Quadratic formula:")
        print()
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print(f"x1 = ( -{b} + sqrt({b} ** 2 - 4 * {a} * {c}) ) / 2 * {a}")
        print('x1 = ', x1)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print(f"x1 = ( -{b} - sqrt({b} ** 2 - 4 * {a} * {c}) ) / 2 * {a}")
        print('x2 = ', x2)
        print()
        print(f"'x1' must be = {(x1 ** 2) + ((6 * x1) + 9)} for 'y' to be 0.")
        print(f"'x2' must be = {(x2 ** 2) + ((6 * x2) + 9)} for 'y' to be 0.")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = len("python")
dragon = len("dragon")
if not python:
    print("Python is Truthy")
else:
    print("Not Python is Falsy")

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in "python" and "dragon":
    print("'on' is in both 'python' and 'dragon'")
else:
    print("'on' is not in both 'python' and 'dragon'")

# 14. "I hope this course is not full of jargon". Use in operator to check
#     if jargon is in the sentence.
if 'jargon' in "I hope this course is not full of jargon":
    print("Yes, 'jargo' is in the sentence")
else:
    print("No, 'jargo' is not in the sentence")

# 15. There is no 'on' in both dragon and python
print("this sentence is not correct")

# 16. Find the length of the text python and convert the value to float
#     and convert it to string
len_python = str(float(len("python")))
print(len_python)
print(type(len_python))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check
#     if a number is even or not using python?
number = 10
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
value = "2.7"
int_value = int(float(value))
floor_division = 7 // 3
if floor_division == value:
    print(f"{floor_division} is equal to {value}")
else:
    print(f"{floor_division} is not equal to {value}")

# 19. Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print(f"{type('10')} is equal to {type(10)}")
else:
    print(f"{type('10')} is not equal to {type(10)}")

# 20. Check if int('9.8') is equal to 10
print(f"int('9.8') cannot be converted to int, because is a float")
print(f"int(float('9.8')) = {int(float('9.8'))} which is not equal to {10}")

# 21. Write a script that prompts the user to enter hours and rate per hour.
#     Calculate pay of the person?
#       Enter hours: 40
#       Enter rate per hour: 28
#       Your weekly earning is 1120

print(" Let's calculate your weekly earnings")
print("--------------------------------------")
hours = float(input("Enter how many hours you've work this week: "))
rate = float(input("Enter rate per hour: "))
weekly_earnings = hours * rate
print(f"Your weekly earnings is: {int(weekly_earnings)}€")

# 22. Write a script that prompts the user to enter number of years.
#     Calculate the number of seconds a person can live (Assuming 100 years)
#     Enter number of years you have lived: 100
#     You have lived for 3153600000 seconds.

one_minute = 60  # seconds
one_hour = 60 * one_minute
one_day = 24 * one_hour
one_year = 365 * one_day

years = float(input("Enter number of years you have lived: "))
years_in_seconds = years * one_year
years_in_seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {int(years_in_seconds)} seconds")

# 23. Write a Python script that displays the following table
#       1 1 1 1 1
#       2 1 2 4 8
#       3 1 3 9 27
#       4 1 4 16 64
#       5 1 5 25 125

for i in range(1, 6):
    a = i
    b = 1
    c = a * b
    d = a * c
    e = a * d
    print(f"{a} {b} {c} {d} {e}")

print()

for i in range(1, 6):
    a = i * i
    b = i * a
    print(f"{i} {1} {i} {a} {b}")

print()

for i in range(1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")
