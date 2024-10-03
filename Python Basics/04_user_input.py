# User Input
print("User Input")

'''
In Python, you can take input from the user using the built-in input() function. 
This function allows you to prompt the user for input, and it always returns the input as a string. 
If you need the input in another data type, such as an integer or float, you'll need to explicitly convert the input.
'''
# 1. Simple Input Example
name = input("Enter your name: ")
print(name)
print(type(name)) # <class 'str'>

'''
2. Converting Input to Other Types
Since input() always returns a string, if you need a numeric value, you can convert it using int(), float(), or other conversion functions.
'''
number = int(input("Enter a number: "))
print(number + 6)
print(type(number)) # <class 'int'>

'''
3. Multiple Inputs
You can take multiple inputs from the user in various ways.
'''
# 3.1. Separate inputs: If you want to collect multiple inputs separately:
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Full Name: {first_name} {last_name}")

# 3.2. Single-line multiple inputs (using split()):
# You can also prompt the user for multiple values in a single line and split them into separate variables.
x, y = input("Enter two numbers separated by a space: ").split()
print(f"First number: {x}, Second number: {y}")