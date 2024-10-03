# Exception handling in Python
print("Exception handling in Python")

'''
Exception handling in Python is a mechanism to catch and handle runtime errors 
or exceptions that may occur during the execution of a program. 
By using exception handling, you can prevent your program from crashing when 
an error occurs and allow it to recover or perform alternative actions.
'''
# 1: Basic Exception Handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input, please enter a number.")

# 2: Catching Multiple Exceptions
# You can catch multiple types of exceptions in a single except block or by using multiple except blocks.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except (ZeroDivisionError, ValueError) as e:
    print(f"Error occurred: {e}")

# 3: Using finally Block
# The finally block is always executed, whether an exception is raised or not.
# It's often used for cleanup actions, like closing files or releasing resources.
try:
    a = open("test.txt", "r")
    data = a.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Closing file.")
    a.close()  # Always executed
