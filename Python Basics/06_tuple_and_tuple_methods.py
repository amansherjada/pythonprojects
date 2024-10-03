# Tuples
print("Tuples in Python")
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

'''
A tuple is an ordered, immutable (unchangeable) collection of elements in Python. 
Tuples are similar to lists, but the key difference is that once a tuple is created, 
you cannot modify its elements (i.e., you cannot add, remove, or change items).

Once a tuple is created, you cannot change its elements.
Tuples maintain the order of elements.
Tuples can have duplicate elements.
Tuples can hold elements of different data types (integers, strings, etc.).
'''
# Tuples are defined using parentheses () and can hold multiple elements
my_tuple = (1, 2, 3, "apple", 5)
print(my_tuple)

# Tuple with one element (important to include a comma after the element):
single_element_tuple = (1,)  # Comma is necessary
print(single_element_tuple)

# Tuple without parentheses (optional): You can also create a tuple without parentheses by separating elements with commas.
my_tuple = 1, 2, 3
print(my_tuple)
print(type(my_tuple))

# fruits[0] = "Aman" (Tuple is immutable and hence this line will throw an Error)

# Accessing Tuple Elements: You can access elements of a tuple using indexing, similar to lists.
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry (negative indexing starts from the end)

# Tuple Slicing:
# You can also slice tuples, returning a new tuple that contains a portion of the original tuple.
fruits = ("apple", "banana", "cherry", "date")
print(fruits[1:3])  # Output: ('banana', 'cherry')

# Tuple Methods in Python
# Since tuples are immutable, they have fewer methods compared to lists.

# 1. count(item): Returns the number of times an item appears in the tuple.
a = (1,2,4,5,7,6,4)
print(a.count(4)) #Output: 2

# 2. index(item): Returns the index of the first occurrence of an item in the tuple.
# If the item is not found, it raises a ValueError.
a = (1,2,4,5,7,6,4)
print(a.index(5)) #Output: 3

# Tuple Operations
# Even though tuples are immutable, you can perform several operations on them without modifying their contents:

# Concatenation (+)
# You can combine two or more tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5)

# Repetition (*)
# You can repeat a tuple multiple times using the * operator.
my_tuple = (1, 2)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# Tuple Length (len())
# You can find the number of elements in a tuple using the len() function.
my_tuple = (1, 2)
print(len(my_tuple)) #Output: 2

# Tuple Membership (in / not in)
# You can check if an item exists in a tuple using in or not in keywords.
fruits = ("apple", "banana", "cherry")
print("apple" in fruits)  # Output: True
print("orange" not in fruits)  # Output: True
print("watermelon" in fruits) # Output: False
print("apple" not in fruits)  # Output: False

'''
Tuples are immutable (cannot be modified once created), while lists are mutable (can be modified). 
If you need a collection that shouldn't be changed, use a tuple.
'''