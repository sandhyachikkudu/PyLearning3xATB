# square and cube of the user input number
import math
x = input("Enter the number\t")
x = int(x)
print(x ** 2)
print(x ** 3)
a = math.sqrt(x)
print(a)
b = math.cbrt(x)
print(b)


## 2 # findnding the greater and lesser numbers

x = input("Enter the first number\t")
y = input("Enter the first number\t")
x = int(x)
y = int(y)
if x > y:
    print("x is greater than y")
    print(x)
else:
    print("y is greater than x")
    print(y)
