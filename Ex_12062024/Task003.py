# 3. Factorial
# # n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24

num = int(input("Enter a number: "))
factorial = 1
# x = 1
# for i in range (1,num+1) :
#     x = x * i
#     print(f"the factorial of {num} is {x}")


while (num > 0):
    factorial = factorial*num
    num =num - 1
print(f"The factorial of 5 is {factorial}")