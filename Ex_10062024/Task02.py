# square and cube of the user input number
import math
x = input("Enter the number\t")
x = float(x)
print(x ** 2)
print(x ** 3)
a = math.pow(x, 2)
print(a)
b = math.pow(x, 3)
print(b)

## 2 # findnding the greater and lesser numbers

x = input("Enter the first number\t")
y = input("Enter the first number\t")
x = int(x)
y = int(y)
if x > y:
    print("x is greater than y")
    print(x)
elif x < y :
    print("y is greater than x")
    print(f"{y} is greater than {x}")
    print(y)
else:
    print("x and y are equal")
