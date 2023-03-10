#  Comparison Operators

"""
Comparison
Operators   Name                        Example
==          Equal                       x == y
!=          Not equal                   x != y
>           Greater than                x > y
<           Less than                   x < y
>=          Greater than or equal to    x >= y
<=          Less than or equal to       x <= y
"""
# Examples:
print('Comparison (3 == 2):', 3 == 2)
print('Comparison (3 != 2):', 3 != 2)
print('Comparison (3 > 2): ', 3 > 2)
print('Comparison (3 < 2): ', 3 < 2)
print('Comparison (3 >= 2):', 3 >= 2)
print('Comparison (3 <= 2):', 3 <= 2)
print()
print("Comparison (len('mango') == len('avocado')):",
      len('mango') == len('avocado'))
print()
print('Comparison (True == True):  ', True == True)
print('Comparison (True == False): ', True == False)
print('Comparison (False == False):', False == False)

print()
print('1 is 1:', 1 is 1)            
print('1 is not 2:', 1 is not 2)    
print('A in David:', 'A' in 'David') 
print('v in David:', 'v' in 'David') 
print("'coding' in 'coding for all': ", 'coding' in 'coding for all') 
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2:', 4 is (2 ** 2))

# Logical Operators
"""
Logical
Operators   Description                 Examples
and         Returns True if both        x < 5 and x > 10
            statements are true

or          Returns True if any         x < 5 or x < 4
            of the statements is true
            
not         Reverses the result         not(x < 5 and x > 10)
            Returns false if true
"""
# Examples:
print()
print("3 > 2 and 4 > 3:", 3 > 2 and 4 > 3)
print('True and True:', True and True)
print('True or False:', True or False)
print("not True:", not True)
print("not not True:", not not True)
print()
print("### Truth table ###")
print("True and True : ", True and True)
print("True and False :", True and False)
print("False and False:", False and False)
print("True or True : ", True or True)
print("True or False: ", True or False)
print("False or False:", False or False)
print()
print("True nand True : ", not(True and True))
print("True nand False :", not(True and False))
print("False nand False:", not(False and False))
print("True xor True : ", not(True or True))
print("True xor False: ", not(True or False))
print("False xor False:", not(False or False))
