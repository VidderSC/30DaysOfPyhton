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
