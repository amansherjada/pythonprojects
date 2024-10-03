print("Hello World!")
print("Hello World!")

'''
Variables in Python
Variables in Python are essentially containers that store data.
They hold information that can be referenced and manipulated within a program.
'''
x = 10  # x is an integer
print(x)
y = "Hello"  # y is a string
print(y)
x = 6.6 # Now, x is a float
print(x)
z =  True # z is a boolean
print(z)
z = None # Now, z is a None
print(z)

'''
Typecasting in Python
Also known as type conversion, is the process of converting one data type into another. 
'''

# 1. Implicit Typecasting (Automatic)
'''
In implicit typecasting, Python automatically converts one data type to another without user intervention.
'''
a = 10   # Integer
b = 3.5  # Float

result = a + b  # Implicit typecasting happens here
print(result)   # Output: 13.5

# x (an integer) is automatically converted to a float

# 2. Explicit Typecasting (Manual)
'''
In explicit typecasting, the user manually converts one data type to another using Python's type conversion functions.
int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
list(): Converts a value to a list.
tuple(): Converts a value to a tuple.
bool(): Converts a value to a boolean.
'''
# Convert float to int
x = 7.8
y = int(x)  # Explicit typecasting
print(y)    # Output: 7 (the decimal part is truncated)

# Convert string to int
a = "123"
b = int(a)  # Explicit typecasting
print(b)    # Output: 123 (now an integer)

# Convert int to string
c = 50
d = str(c)  # Explicit typecasting
print(d)    # Output: "50" (now a string)
print(type(d)) # <class 'str'>
'''
Invalid conversion
a = "123abc"
b = int(a)  # Raises ValueError because the string contains non-numeric characters
'''