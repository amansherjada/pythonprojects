# Lists
print("Lists in Python")

'''
A list in Python is a collection of items (elements) that can store multiple values in a single variable. 
Lists are ordered, mutable (modifiable), and can contain elements of different data types (e.g., integers, strings, or even other lists).
'''
my_list = [1, 2, 3, "apple", [5, 6]]
print(my_list)

# List Indexing:
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry (negative indexing starts from the end)

# List Slicing:
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[1:3])  # Output: ['banana', 'cherry']

# List Methods in Python
print("List Methods in Python")

# 1. append(item): Adds an item to the end of the list.
print("1. append()")
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 2. insert(index, item): Inserts an item at a specified index.
print("2. insert(index, item)")
fruits = ["apple", "banana"]
fruits.insert(1, "watermelon")
print(fruits) # Output: ['apple', 'watermelon', 'banana']

# 3. remove(item): Removes the first occurrence of a specified item.
print("3. remove(item)")
fruits = ["apple", "banana"]
fruits.remove("apple")
print(fruits) #Output: ['banana']

# 4. pop([index]): Removes and returns the item at the specified index.
# If no index is provided, it removes and returns the last item.
print("4. pop([index])")
fruits = ["apple", "banana"]
fruits.pop()
print(fruits) #Output:['apple']

fruits = ["apple", "banana"]
fruits.pop(0)
print(fruits) #Output:['apple']

# 5. clear(): Removes all elements from the list.
print("5. clear()")
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []

# 6. index(item): Returns the index of the first occurrence of an item.
print("6. index(item))")
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1

# 7. count(item): Returns the number of occurrences of a specific item in the list.
print("7. count(item)")
fruits = ["apple", "banana", "banana","cherry"]
print(fruits.count("banana"))  # Output: 2

# 8. sort(): Sorts the list in ascending order.
# You can also use the reverse=True parameter to sort in descending order.
print("8. sort()")
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]

# 9. reverse(): Reverses the order of the list.
print("9. reverse()")
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

numbers = [3, 1, 4, 2]
numbers.reverse()
print(numbers) # Output: [2, 4, 1, 3]

# 10. copy(): Returns a shallow copy of the list.
print("10. copy()")
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits)  # Output: ['apple', 'banana', 'cherry']

# 11. extend(iterable)
# Extends the list by adding all the items from an iterable (e.g., another list, tuple, etc.).
fruits = ["apple", "banana"]
more_fruits = ["cherry", "date"]
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# List methods Docs (https://docs.python.org/3/tutorial/datastructures.html)

# Common List Operations

# List Length (len())
# You can find the number of elements in a list using the len() function.
fruits = ["apple", "banana", "cherry"]
print("Length of the List is:",len(fruits))  # Output: 3

# List Repetition (*)
# You can repeat a list multiple times using the * operator.
list1 = [1, 2]
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 1, 2, 1, 2]

# List Concatenation (+)
# You can concatenate two lists using the + operator.
list1 = [1, 2, 3]
list2 = [4, 5]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5]