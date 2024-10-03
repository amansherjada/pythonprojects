# Sets in Python
print("Sets in Python")
empty_set = set() # Cannot use {} because it creates an empty dictionary
print(empty_set)
print(type(empty_set))

'''
A set is an unordered collection of unique elements in Python. 
Sets are useful for storing multiple items in a single variable, especially when you want to ensure that no duplicates are present.
They are defined using curly braces {} or the set() constructor.
'''
my_set = {1, 2, 3, "apple", "banana"}
print(my_set)

my_set = set([1, 2, 3, 4, 4])  # Duplicate '4' will be removed
print(my_set)  # Output: {1, 2, 3, 4}

# Accessing Elements in a Set:
# Since sets are unordered, you cannot access elements by index.
# However, you can loop through the elements of a set:
my_set = {1, 2, 3, "apple"}
for item in my_set:
    print(item)

# Set Methods in Python
# Sets provide several methods that allow you to perform various operations, including adding, removing, and checking membership.
# Here are some commonly used set methods:

# 1. add(item)
# Adds an item to the set. If the item is already present, it does nothing.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
my_set.add(2)  # No change since '2' is already in the set
print(my_set)  # Output: {1, 2, 3, 4}

# 2. remove(item)
# Removes an item from the set. Raises a KeyError if the item is not found.
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
# my_set.remove(4)  # Would raise KeyError

# 3. discard(item)
# Removes an item from the set if it exists.
# Does not raise an error if the item is not found.
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
my_set.discard(4)  # No error even though '4' is not in the set
print(my_set)  # Output: {1, 3}

# 4. pop()
# Removes and returns an arbitrary element from the set.
# Raises a KeyError if the set is empty.
my_set = {1, 2, 3}
item = my_set.pop()
print(item)  # Output: One of the elements (1, 2, or 3)
print(my_set)  # Remaining elements

#5. clear()
# Removes all items from the set.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# 6. union(set2) or | operator
# Returns a new set that is the union of two sets (combines elements from both sets).
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Using the | operator
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# 7. intersection(set2) or & operator
# Returns a new set containing elements common to both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
# Using the & operator
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

# 8. difference(set2) or - operator
# Returns a new set containing elements in the first set that are not in the second set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
difference_set = set2.difference(set1)
print(difference_set)  # Output: {4, 5}
# Using the - operator
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# 9. symmetric_difference(set2) or ^ operator
# Returns a new set containing elements that are in either of the sets, but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}
# Using the ^ operator
symmetric_diff_set = set1 ^ set2
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}

# 10. copy()
# Returns a shallow copy of the set.
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)  # Output: {1, 2, 3}