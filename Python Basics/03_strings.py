# String Methods (https://docs.python.org/3/library/stdtypes.html#string-methods)
print("String Methods")

'''
1. capitalize()
Converts the first character of a string to uppercase and the rest to lowercase.
'''
print("1. capitalize()")
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

'''
2. lower()
Converts all characters in the string to lowercase.
'''
print("2. lower()")
text = "HELLO"
print(text.lower())  # Output: "hello"

'''
3. upper()
Converts all characters in the string to uppercase.
'''
print("3. upper()")
text = "hello"
print(text.upper()) # Output: "HELLO"

'''
4. title()
Converts the first letter of each word to uppercase and the remaining letters to lowercase.
'''
print("4. title()")
text = "hellO worLd"
print(text.title())  # Output: "Hello World"

'''
5. strip()
Removes leading and trailing whitespace (or specified characters).
'''
print("5. strip()")
text = "   hello   "
print(text.strip())  # Output: "hello"

# You can also pass specific characters to remove:
text = "###hello###"
print(text.strip("#"))  # Output: "hello"

'''
6. replace(old, new)
Replaces all occurrences of a substring with a new string.
'''
print("6. replace(old, new)")
text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"

'''
7. split(sep)
Splits a string into a list where each word is a list item, separated by a specified delimiter (default is space).
'''
print("7. split(sep)")
text = "apple,banana,orange"
print(text.split(","))  # Output: ['apple', 'banana', 'orange']

'''
8. join(iterable)
Joins the elements of an iterable (like a list) into a string, using the specified separator.
'''
print("8. join(iterable)")
fruits = ['apple', 'banana', 'orange']
print(", ".join(fruits))  # Output: "apple, banana, orange"

# For more strings methods refer python docs (https://docs.python.org/3/library/stdtypes.html#string-methods)