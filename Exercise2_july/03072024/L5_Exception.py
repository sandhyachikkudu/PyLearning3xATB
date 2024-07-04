
try:
    # while True print("hello")
    10/0
except Exception as e:
    print(e)



# error are something, which is difficult to recover
# errors are more sever issue that typically prevent the program from running
# impossible to recover the program


# exceotion (error)--> can be handled
# exception are events occur during the execution a program
# that distrupt the flow of instruction
# possible to recover the program


import math
# math.exp(1000)   OverflowError: math range error

# exception handling
try:
    import math
    math.exp(1000)

except Exception as e:
    print(e)