# try:
#     # code
# except Exception as e:
#     print(e)


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c=a/b
    print("the result",c)
except Exception as e:
    print(e)
    print("Error--please enter integer")


print("end of the program")

# o/p
# Enter a number: ewq
# invalid literal for int() with base 10: 'ewq'
# Error--please enter integer
# end of the program