my_dict = {
    'name' : 'sand',
    'grade': 'A',
    'age' : 23
}


for k,v in my_dict.items():
    print(f"keys are {k} and the values are {v}")


for k,v in my_dict.items():
    if k=='grade':
        print("this is in dic")


op = 'grade' in my_dict
print(op)