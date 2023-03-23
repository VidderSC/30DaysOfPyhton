# Day 3 - 30DaysOfPython Challenge

# Operators
"""
Assignment                              Arithmetic
Operator:   Example     Same As         Operator:
=           x = 5       x = 5           Asignment (=)
+=          x += 5      x = x + 5       Addition (+)
-=          x -= 5      x = x - 5       Substraction (-)
*=          x *= 5      x = x * 5       Multiplication (*)
/=          x /= 5      x = x / 5       Division (/)
%=          x %= 5      x = x % 5       Modulus (%)
//=         x //= 5     x = x // 5      Floor division (//)
**=         x **= 5     x = x ** 5      Exponentiation (**)

Bitwise Operators (Used to compare binary numbers)
&=          x &= 5      x = x & 5       (and)
|=          x |= 5      x = x | 5       (or)
^=          x ^= 5      x = x ^ 5       (xor)
>>=         x >>= 5     x = x >> 5      (Signed right shift)
<<=         x <<= 5     x = x << 5      (Zero fill left shift)
"""

# Arithmetic operations
# Integers:
print('Addition (1 + 2): ', 1 + 2)                  # 3
print('Substraction (2 - 1): ', 2 - 1)              # 1
print('Multiplication (2 * 3): ', 2 * 3)            # 6
# 2.0  Division in Python returns float
print('Division (4 / 2): ', 4 / 2)
print('Division (7 / 2): ', 7 / 2)                  # 3.5
# 3  Returns Integer, without remainder
print('Division w/ remainder (7 // 2): ', 7 // 2)
# 1  Returns Integer, just the remainder
print('Modulus (3 % 2): ', 3 % 2)
print('Exponentation (2 ** 3): ', 2 ** 3)           # 9  Same as 2 * 2 * 2
# Floats:
print()
print('Floating Point Number, PI:', 3.14)
print('Floating Point Number, Gravity:', 9.81)
# Complex numbers:
print()
print('Complex Number (1 + 1j): ', 1 + 1j)
print('Multiplying complex numbers [(1 + 1j)*(1 - 1j)]: ', (1 + 1j) * (1 - 1j))

# For this example we are going to use single character variable but remember
# do not develop a habit of declaring such types of variables.
# Variable names should be all the time mnemonic.
print()
# We declare the variables always at the top of the code.

a = 3  # Integer
b = 2  # Integer

total = a + b  # We didn't use sum instead of total because 'sum' is a buit-in function
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# If you do not label your print, you never know where its coming from.
print(total)
print('a = ', a)
print('b = ', b)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
print()

print('== Addition, Substraction, Multiplication, Division, Modulus ==')
num_one = 3
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

print('num_one = ', num_one)
print('num_two = ', num_two)
print('total (num_one + num_two): ', total)
print('difference (num_one - num_two): ', diff)
print('product (num_one * num_two): ', product)
print('division (num_one / num_two): ', div)
print('remainder (num_one % num_two): ', remainder)

# Examples:
print()
print('-- Examples:')
print('- Calculating the Area of a circle:')
radius = 10
PI = 3.14
area_of_circle = PI * radius ** 2
print('radius =', radius)
print('PI = ', PI)
print('Area (PI * radius ** 2):', area_of_circle)

print()
print('- Calculating the Area of a rectangle:')
length = 10
width = 20
area_of_rectangle = length * width
print('length =', length)
print('width =', width)
print('Area (length * width):', area_of_rectangle)

print()
print('- Calculating the Weight of an object:')
mass = 75
gravity = 9.81
weight = mass * gravity
print('mass =', mass)
print('gravity = ', gravity)
print('Weight = (mass * gravity):', weight, 'N')  # Added the unit

print()
print('- Calculating the density of a liquid:')
mass = 75   # in Kg
volume = 0.075  # in cubic meter
density = mass / volume  # 1000 Kg/m^3
print('mass =', mass)
print('volume = ', volume)
print('Density = (mass / volume):', density, 'Kg/m^3')
