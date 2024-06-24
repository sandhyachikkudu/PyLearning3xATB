def anagram(name,name1):
    name=name.lower().replace(' ','')
    name1=name1.lower().replace(' ','')
    if len(name)==len(name1):
        print(name+' is anagram of '+name1)
        return True
    else:
        print(name+' is not anagram of '+name1)
        return False


d=anagram('silent','listen')

name = input("Enter your name: ")
name1 = input("Enter your first name: ")
name=name.lower().replace(' ','')
name1=name1.lower().replace(' ','')
if len(name)==len(name1):
    print(name+' is anagram of '+name1)
else:
    print(name+' is not anagram of '+name1)