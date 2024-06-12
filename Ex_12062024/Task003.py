# 3. Factorial
# # n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24

num = int(input("Enter a number: "))
x = 1
for i in range (1,num+1) :
    x = x * i
    print(f"the factorial of {num} is {x}")
