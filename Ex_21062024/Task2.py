def palindrome(name):
    name = name.replace(" ", "").lower()
    name1 = name[::-1]
    name1 = name1.replace(" ", "").lower()
    if name == name1:
        print("palindrome")
    else:
        print("not palindrome")


a = palindrome("nitin")




name3 = input("enter your name:")
name3 = name3.replace(" ", "").lower()
name2 = name3[::-1]
if name2 == name3[::-1]:
    print("p")

else:
    print("np")