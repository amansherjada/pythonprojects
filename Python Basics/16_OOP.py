# Object-Oriented Programming (OOP) in Python
print("Object-Oriented Programming (OOP) in Python")

'''
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects rather 
than functions and logic. Python is an object-oriented language, and OOP allows developers to structure their code 
using classes and objects to model real-world entities.

Core Concepts of OOP in Python:
1. Class: A blueprint for creating objects. It defines attributes and methods that the objects will have.
2. Object: An instance of a class. It represents a specific entity with attributes and behaviors defined by the class.
3. Attributes (or Properties): Variables that store data for an object (e.g., name, age).
4. Methods: Functions defined inside a class that describe the behaviors of an object.
'''

# 1. Classes and Objects:
# A class defines a blueprint for objects.
# Objects are instances of a class. You create a class using the `class` keyword.

# Define a class named 'Person'
class Person:
    # Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age  # Attribute

    # Method of the class
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance of the class)
person1 = Person("Alice", 25)  # Instantiate object with name and age

# Accessing attributes
print(person1.name)  # Output: Alice
print(person1.age)  # Output: 25

# Calling a method
person1.greet()  # Output: Hello, my name is Alice and I am 25 years old.