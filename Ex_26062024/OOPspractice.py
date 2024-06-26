class Dog:
    name = None
    id = None


    def __init__(self,name,id):
        self.name = name
        self.id = id


    def sleep(self):
        print("who is sleeping--->"+self.name)



dog1 = Dog("chow",1)
dog2 = Dog("mow",2)
print(f"{dog1.name} has id {dog1.id}")
print(f"{dog2.name} has id {dog2.id}")
dog1.sleep()
dog2.sleep()


