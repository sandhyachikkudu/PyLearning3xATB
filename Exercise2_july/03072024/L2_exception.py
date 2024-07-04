a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c=a/b
print("the result",c)

# Enter a number: 12
# Enter another number: 0
# Traceback (most recent call last):
#   File "C:\Users\user\PycharmProjects\PyLearning3xATB\Exercise2_july\L2_exceotion.py", line 3, in <module>
#     c=a/b
#       ~^~
# ZeroDivisionError: division by zero


# Enter a number: true
# Traceback (most recent call last):
#   File "C:\Users\user\PycharmProjects\PyLearning3xATB\Exercise2_july\L2_exceotion.py", line 1, in <module>
#     a = int(input("Enter a number: "))
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'true'



# ATM --> SBI
# ATM->SBI->inserted the card-->10k withdraw
# inserted the card--->amount-->entered the pin --->money got deducted
# but the money not received from ATm via ATM(not handled properly)

# by this -- bad user experiance
# user will curse
# we need to handle this and give user better experiance