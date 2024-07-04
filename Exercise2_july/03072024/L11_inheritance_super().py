class Parent:
    def __init__(self):
        print("i am a Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("i am a Child")

son = Child()