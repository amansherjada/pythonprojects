# For Loop in Python
print("For Loop in Python")

'''
In Python, a for loop is used to iterate over a sequence 
(such as a list, tuple, string, or range) and execute a block of code 
for each element in that sequence
'''

# Iterating Over a List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#  Iterating Over a String
name = "Aman"

for letter in name:
    print(letter)

# Using range() in a For Loop
# The range() function generates a sequence of numbers,
# and it's often used in for loops to control how many times the
# loop should run.
for i in range(5):
    print(i)

for i in range(1, 11):
    print(2 * i)

# Specifying Start, Stop, and Step with range()
# You can also specify a starting value, stopping value,
# and step size with the range() function.
for i in range(2, 11, 2):
    print(i)
# range(2, 11, 2) generates numbers starting from 2, ending at 10 (11 is excluded), and increments by 2 each time.

# Nested for Loop
# You can use for loops inside other for loops to iterate over
# multiple sequences or to work with multidimensional data.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# Breaking Out of a for Loop
# You can use the break statement to exit a for loop prematurely when a certain condition is met.
for i in range(1, 6):
    if i == 3:
        break
    print(i)
