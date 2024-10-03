# File I/O in Python
print("File I/O in Python")

'''
File I/O (Input/Output) in Python allows a program to interact with files for 
reading, writing, or appending data. 
File handling is essential for tasks like saving data to 
files, reading data from files, and managing file content.
'''
# Writing to a file and reading it

# Write some content to the file
with open("data.txt", "w") as file:
    file.write("Python File Handling Example.\n")
    file.write("This is the second line.\n")

# Read the file content
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Append a new line and read it again
with open("data.txt", "a") as file:
    file.write("This line is appended.\n")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)