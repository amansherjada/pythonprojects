# Operators in Python are special symbols or keywords used to perform operations on variables and values.
print("Operators in Pyton")

'''
1. Arithmetic Operators
Arithmetic operators are used for performing mathematical operations like addition, subtraction, multiplication, and division.
'''
print("1. Arithmetic Operators")
x = 10
y = 3
print(x + y)   # Addition Output: 13
print(x - y)   # Subtraction Output: 7
print(x * y)   # Multiplication Output: 30
print(x / y)   # Division (float result) Output: 3.3333333333333335
print(x // y)  # Floor Division (integer result) Output: 3 (integer division)
print(x % y)   # Modulus (remainder) Output: 1 (remainder)
print(x ** y)  # Exponentiation (power) Output: 1000 (10 raised to the power of 3)
print("x + y is:", x + y)

'''
2. Assignment Operators
Assignment operators are used to assign values to variables.
'''
print("2. Assignment Operators")
x = 10  # Assigns value
x += 5  # Add and assign (Equivalent to x = x + 5)
print(x) # Output: 10
x -= 5 # Subtract and assign (Equivalent to x = x - 5)
print(x)  # Output: 10
x *= 2   # Multiply and assign (Equivalent to x = x * 2)
print(x)  # Output: 30

'''
3. Comparison Operators
Comparison operators compare two values and return a Boolean result (True or False). 
These are used to compare values.
'''
print('3. Comparison Operators')
x = 5
y = 10
print(x == y)  # Equal to (Output: False)
print(x != y)  # Not equal to (Output: True)
print(x > y)   # Greater than (Output: False)
print(x < y)   # Less than (Output: True)
print(x >= y) # Greater than or equal to (Output: False)
print(x < y) # Less than or equal to (Output: False)

'''
4. Logical Operators
Logical operators are used to combine conditional statements and return a Boolean result (True or False).
'''
print("4. Logical Operators")
x = 10
y = 5
print(x > 5 and y < 10)  # Output: True (both conditions are true) Logical AND
print(x > 5 or y > 10)   # Output: True (one condition is true) Logical OR
print(not (x > 5))       # Output: False (negation of True) Logical NOT
print(not (False))        # Output: True (negation of False) Logical NOT

'''
5. Identity Operators
Identity operators check if two variables refer to the same object in memory.
is = Returns True if both variables point to the same object	        (a is b)
is not = Returns True if variables do not point to the same object      (a is not b)
'''
print("5. Identity Operators")
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)      # Output: True (x and z refer to the same object)
print(x is y)      # Output: False (x and y refer to different objects)
print(x == y)      # Output: True (they have the same values)
print(x is not y)  # Output: True (x and y are not the same object)

'''
6. Membership Operators
Membership operators check if a value exists within a sequence like a 
list, tuple, string, or set.
in = Returns True if the value is present in the sequence	        a in b
not in = Returns True if the value is not present in the sequence	a not in b
'''
print("6. Membership Operators")
x = [1, 2, 3, 4, 5]
print(3 in x)      # Output: True
print(10 not in x) # Output: True
print(1 not in x) # Output: False