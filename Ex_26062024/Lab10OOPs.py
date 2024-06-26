class Dog:
    name= None
    id = None
    # constructors: used to intilize the values of the instance
    # variables(attributes)


    def speak(self):
        print("Sleeping")



doq1 = Dog()
# print(dog1.name)
doq1.name = "chow"
print(doq1.name)
dog2 = Dog()
doq1.speak()
dog2.speak()

class calc:

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

    def pow(self,a,b):
        return a**b

    def sqrt(self,a):
        return a**0.5



object_ref = calc()
print(object_ref)
print(object_ref.sub(1,2))
print(object_ref.mul(2,2))
print(object_ref.div(2,2))






















