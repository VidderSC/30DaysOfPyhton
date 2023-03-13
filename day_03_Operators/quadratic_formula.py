# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values
#     and figure out at what x value y is going to be 0.

from math import sqrt

a = 1
b = 10
c = 9

print(f"y = ({a}*x^2) + ({b}*x) + {c}")
print()

for x in range(5):
    y = (a*x ** 2) + (b*x) + c
    print(f'x = {x}')
    print(f'y = ({a*x**2} + {b*x} + {c}) = {y}')
    print()

print(f"y = ({a}*x^2) + ({b}*x) + {c}")

if a > 0:  # 'a' must be bigger than 0, otherwise won't be not valid.
    # 'b' must be 6 or bigger to work, otherwise will return an error.
    if b >= 6 or b <= -6:
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
            print(f"y = {(a*x**2) + (b*x) + c}")
            print()
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
            print(f"'x1' must be either {x1} or {x2} for 'y' to be 0.")
            print(f"Using 'x1', y = {(a*x1**2) + (b*x1) + c}")
            print(f"Using 'x2', y = {(a*x2**2) + (b*x2) + c}")
            print()
    else:
        print("If 'b' is between -6 and +6, result will be a complex root.")
else:
    print("'a' must be bigger than 0, otherwise it will return an error.")
