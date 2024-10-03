# Dictionary in Python

print("Dictionary in Python")
empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))

'''
A dictionary is an unordered, mutable collection of key-value pairs. 
It is similar to a real-world dictionary where a word (key) maps to a definition (value). 
Each key is unique, and the values associated with the keys can be of any data type. 
Dictionaries are defined using curly braces {} or the dict() constructor.

1. Unordered: Items in a dictionary are not stored in any particular order.
2. Key-Value Pairs: Each item in a dictionary has a key and a corresponding value.
3. Keys are Unique: Duplicate keys are not allowed. If a key is repeated, the last assignment wins.
4. Mutable: Dictionaries can be changed by adding, modifying, or removing key-value pairs.
'''
# 1. Creating a Dictionary:
# 1.1. Creating a Dictionary Using Curly Braces:
my_dict = {"name": "Aman", "age": 23, "city": "Mumbai"}
print(my_dict)
print(type(my_dict)) # <class 'dict'>

# 1.2. Creating a Dictionary Using the dict() Constructor:
my_dict = dict(name="A-man", age=1300, city="Star")
print(my_dict)
print(type(my_dict)) # <class 'dict'>

# 2. Accessing Dictionary Items:
# 2.1. You can access a value by referencing its key inside square brackets or using the get() method.
my_dict = {"name": "Aman", "age": 23, "city": "Mumbai"}
print(my_dict["name"]) # Output: Aman
print(my_dict.get("age")) # Output: 23

# 2.2. If you try to access a key that doesn’t exist, using square brackets will raise a KeyError,
# while get() returns None.
print(my_dict.get("country"))  # Output: None
# print(my_dict["country"])  # Raises KeyError

# 3. Modifying a Dictionary:
# 3.1 Changing Values: You can update the value associated with a specific key.
my_dict["age"] = 26
print(my_dict) # Output: {'name': 'Aman', 'age': 26, 'city': 'Mumbai'}

# 3.2. Adding New Key-Value Pairs:
# If the key does not exist, assigning a value to it will add it to the dictionary.
my_dict["country"] = "India"
print(my_dict) # Output: {'name': 'Aman', 'age': 26, 'city': 'Mumbai', 'country': 'India'}

# 4. Dictionary Methods in Python
print("Dictionary Methods in Python")

# 4.1. clear()
# Removes all key-value pairs from the dictionary, resulting in an empty dictionary.
my_dict.clear()
print(my_dict)  # Output: {}

# 4.2. copy()
# Returns a shallow copy of the dictionary.
my_dict = {"name": "Aman", "age": 23}
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'name': 'Aman', 'age': 23}

# 4.3. fromkeys(keys, value)
# Creates a new dictionary with the specified keys, all set to the provided value.
keys = ["name", "age", "city"]
value = None
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # Output: {'name': None, 'age': None, 'city': None}

# 4.4. get(key, default)
# Returns the value for the specified key.
# If the key is not found, it returns the provided default value (or None if no default is given).
print(my_dict.get("age")) # Output: 23
print(my_dict.get("place", "Unknown"))  # Output: Unknown

# 4.5. items()
# Returns a view object that displays a list of dictionary’s key-value pairs as tuples.
print(my_dict.items()) #Output: dict_items([('name', 'Aman'), ('age', 23)])

# 4.6. keys()
# Returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys()) # Output: dict_keys(['name', 'age'])

# 4.7. values()
# Returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values()) # Output: dict_values(['Aman', 23])

# 4.8. pop(key, default)
# Removes the key and returns its value. If the key does not exist,
# it returns the provided default value (or raises a KeyError if no default is given).
my_dict = {"name": "John", "age": 30}
age = my_dict.pop("age")
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'John'}

# 4.9. popitem()
# Removes and returns the last inserted key-value pair as a tuple.
# Since Python 3.7+, dictionaries maintain the order of insertion.
my_dict = {"name": "John", "age": 30}
item = my_dict.popitem()
print(item)  # Output: ('age', 30)
print(my_dict)

# 4.10. setdefault(key, default)
# Returns the value of the specified key.
# If the key does not exist, it inserts the key with the specified default value.
my_dict = {"name": "John", "age": 30}
city = my_dict.setdefault("city", "New York")
print(city)  # Output: New York
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# 4.11. update(dictionary)
# Updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs.
my_dict = {"name": "John", "age": 30}
my_dict.update({"age": 56, "city": "Jamaica"})
print(my_dict)  # Output: {'name': 'John', 'age': 56, 'city': 'Jamaica'}

'''
Use Cases of Dictionaries:
Storing related information: When you need to store associated data, like user profiles or product information.

Counting occurrences: Dictionaries are commonly used to count the occurrences of items in a list.
'''

# Dictionary Docs = https://docs.python.org/3/tutorial/datastructures.html#dictionaries