# file IO

with open('pramod.txt','r') as file:
    print(file.read())
    file.close()

print("-----------")
try:
    with open('pramod.txt','r') as file:
        print("opened the file")
        print(file.read())

except FileNotFoundError as fnfe:
    print(fnfe)

finally:
    print("closing the file")
    file.close()


print("-----------")


try:
    with open('example.txt','r') as file:
        print("opened the file")
        print(file.read())

except FileNotFoundError as error:
    print("I am not ale to find the file, please check path ,")

finally:
    print("closing the file")
    file.close()