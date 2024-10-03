# match-case Statement
print("match-case Statement")

'''
In Python 3.10 and later, the match-case statement was introduced as a more versatile alternative
to chained if-elif-else statements.
It allows you to match specific values or patterns and execute code based on the matched case.
'''

day = input("Enter a day of the week: ").lower()

match day: # You specify the variable or expression you want to match against different patterns.
    case "monday": #  These represent the different patterns or values you want to check for.
        print("Start of the work week!")
    case "friday":
        print("Almost the weekend!")
    case "saturday" | "sunday":  # Multiple cases combined
        print("It's the weekend!")
    case _: # The underscore (_) serves as a wildcard or default case (equivalent to [else] in if-else).
        print("Mid-week days.")
