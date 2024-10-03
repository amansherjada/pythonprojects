# Functions in Python
print("Functions in Python")

'''
In Python, a function is a block of reusable code designed to perform a specific task. 
Functions allow you to organize your code into manageable, modular sections, 
which can be reused to avoid repetition and make your code more maintainable and 
readable.
'''
# 1: Defining and Calling a Simple Function
def greet(): # def: This keyword is used to define a function. greet is a name to uniquely identify the function
    print("Hello, Welcome to Mumbai!")

greet()  # Calling the function

# 2: Function with Parameters
#You can pass data (parameters) to a function when you call it.
# The function can then use that data to perform specific operations.

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Aman")  # Passing "Alice" as the argument
greet_user("Ramesh")    # Passing "Bob" as the argument

# 3: Function with Return Value
# A function can return a value using the return statement.
# This allows the caller of the function to use the result.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

# 4: Default Parameter Values
# You can provide default values for parameters.
# If no argument is passed, the default value will be used.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Uses default value
greet("Ramu")  # Uses provided argument

# 6: *args (Arbitrary Arguments)
# You can use *args to pass a variable number of arguments to a function.
# Inside the function, args is treated as a tuple.
# The *args allows the function to accept any number of arguments.
def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)

# 7. **kwargs (Keyword Arguments)
# Similarly, **kwargs allows you to pass a variable number of keyword arguments.
# Inside the function, kwargs is treated as a dictionary.
# The **kwargs collects keyword arguments as a dictionary.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")

# 8: Recursive Function
# A function can call itself.
# This is known as recursion, and it is useful for solving problems that can be broken down into smaller, similar subproblems.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)
# The factorial(n) function calls itself to calculate the factorial of a number recursively.