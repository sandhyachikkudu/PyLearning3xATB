# Recursion is a programming technique
# where function calls itself in order
# to solve the problem
# key concept
# base case
# recursive case

def factorial(number):
    # base case
    if number == 0 or number == 1:
        return 1
    # recurdive case
    else:
        return number*factorial(number-1)


print(factorial(5))













