# While Loop
print("While Loop")

'''
A while loop in Python repeatedly executes a block of code as long as a given condition is True. 
It checks the condition before each iteration, and the loop runs as long as the condition remains true. 
Once the condition becomes False, the loop stops.
'''

# 1: Simple while Loop
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment the counter by 1

# The loop continues to run as long as count is less than or equal to 5.
# The variable count is incremented by 1 in each iteration, and the loop stops when count exceeds 5.

# 2: Infinite while Loop
'''
A while loop can become an infinite loop if the condition is never False. 
Be careful to always update the condition within the loop to avoid getting stuck in an infinite loop.
'''
while True:
    print("This will run forever unless you break the loop.")
    break  # This will break the infinite loop

# 3: Using while with User Input
# You can use a while loop to repeatedly prompt for user input until a certain condition is met.

number = 0
while number <= 0:
    number = int(input("Enter a positive number: "))

print(f"Positive number entered: {number}")
# The loop keeps asking for a positive number until the user enters a number greater than 0.

# 4: Breaking Out of a while Loop
number = 1
while number <= 10:
    print(number)
    if number == 5:
        break  # Exit the loop when number is 5
    number += 1

# 5: Skipping an Iteration with continue
# The continue statement can be used inside a while loop to skip the current iteration and move to the next one.
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue  # Skip the rest of the code when number is 3
    print(number)