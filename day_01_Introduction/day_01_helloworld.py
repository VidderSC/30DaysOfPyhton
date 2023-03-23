### Day 1 - 30DaysOfPython Challenge

print(2 + 3)    # addition(+)
print(3 - 1)    # subtraction(-)
print(2 * 3)    # multiplication(*)
print(3 / 2)    # division(/)
print(3 ** 2)   # exponential or power(**)
print(3 % 2)    # modulus(%)
print(3 // 2)   # Floor division operator(//)

# Checking data types
print(type(10))                 # Integer(int)
print(type(3.14))               # float
print(type(1 + 3j))             # Complex number(complex)
print(type(True))               # Boolean(bool)
print(type('Vidders'))            # String(str)
print(type([1, 2, 3]))          # list
print(type({'name': 'Vidders'}))  # Dictionary(dict)
print(type({9.18, 3.14, 2.7}))  # set
print(type((9.18, 3.14, 2.7)))  # tuple

# Exercise: Level 3.2
# Find an Euclidian distance between (2,3) and (10,8)
# In mathematics, the Euclidean distance between two points in Euclidean space is
# the length of a line segment between the two points. It can be calculated from the
# Cartesian coordinates of the points using the Pythagorean theorem.
# It's represented as:
# d(p,q) = |p-q|  /// or d(p,q) = Square Root of (p-q)^2
# Symplyfiying it:
# d(p,q) = absolute(p-q)

print('Euclidean distance of (2,3):', abs(2-3))
print('Euclidean distance of (10,8):', abs(10-8))
