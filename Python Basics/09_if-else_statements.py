# If-Else Statement in Python
print("If-Else Statement in Python")

'''
In Python, the if-else statement allows you to execute a block of code if a condition is true, 
and another block if it is false.
The if block checks a condition. If it evaluates to True, the indented code block after if is executed. 
If it evaluates to False, the code inside the else block runs instead.
'''
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# 2. Elif (Else If) Statement
# The elif statement allows you to check multiple conditions sequentially.
# If the first condition is false, it moves to the next elif condition, and so on.
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Nested If Statements
# You can also use if statements inside another if or else block. This is called nested if statements.
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print(f"{number} is a positive even number.")
    else:
        print(f"{number} is a positive odd number.")
else:
    print(f"{number} is not a positive number.")