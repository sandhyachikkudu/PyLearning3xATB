try:
    with open('testdata.txt','r') as file:

        content = file.readlines()

except FileNotFoundError as fnf:
    print(fnf)

else:
    print(content)

finally:
    print("closing")
    try:
        file.close()
    except NameError as Ne:
        print(Ne)
