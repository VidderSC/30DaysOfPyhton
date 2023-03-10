# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values
#     and figure out at what x value y is going to be 0.

from math import sqrt
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
