import os.path
try:
    file = open('example.txt','r')
    print(file.read())

except FileNotFoundError as fnfe:
    print(fnfe)

finally:
    print("executed")
    try:
        file.close()
    except NameError as ne:
        print(ne)


print("==================")


try:
    file = open('pramod.txt','r')
    print(file.read())

except FileNotFoundError as fnfe:
    print(fnfe)

finally:
    print("executed")
    try:
        file.close()
    except NameError as ne:
        print(ne)

