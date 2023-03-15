import os
import sys
import mymodule
from mymodule import sum_two_nums as suma, person, GRAVITY as g
from statistics import mean, median, mode, stdev
import math
from math import pi as PI
from math import sqrt
import string
from random import random, randint

print(mymodule.generate_full_name('Vidders', 'SC'))  # Vidders SC
print(suma(46, 23))  # 69
print(g)  # 9.807m/s
print(person["firstname"])  # Vidders
print()

print(os.getcwd())
print()

print(sys.path)
print()

sys.path.insert(1, 's:\\30DaysOfPython\\data')

print(sys.path)

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~21.09
print(median(ages))     # 22
print(mode(ages))       # 20
print(stdev(ages))      # ~6.10
print()

print(PI)
print(sqrt(10))
print(10**(1/2))
print(math.pow(2, 3))
print()

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print()

# it doesn't take any arguments; it returns a value between 0 and 0.9999
print(random())
# it returns a random integer number between [5, 20] inclusive
print(randint(5, 20))
