# encapsulation
# wrapping or binding the variables with the methods-encapsulation
# binding the variables with the methods
# hide the data member(class variables,instance variables) only by using methods

class car:
    name = None
    password = "123"

    def __init__(self):
        print("i am called when object is created")

    def chage_password(self):
        self.password = input("Enter your password: ")
        return self.password

xuv = car()
xuv.chage_password()
xuv.password = '345'
print(xuv.chage_password())