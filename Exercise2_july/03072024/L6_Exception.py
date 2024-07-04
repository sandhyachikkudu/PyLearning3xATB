# try,except,finally

try:
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))
    result = num1/num2
except Exception as ve:
    print(ve)
except ZeroDivisionError as zDe:
    print(zDe)

else:
    print(f"result is:{result}")

finally:
    print("i will executed anyhow!!")