class student:

    def __init__(self):
        self.name = input("Enter your name:")
        self.age = int(input("enter your age"))


    def display(self):
        print(f"{self.name} age is {self.age}")


student1=student()
student1.display()