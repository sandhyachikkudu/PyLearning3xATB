class person:
    # Attribute
    name = None
    id = None
    Age = None
    phone_number = None
    # Behaviour
    def talk(self):
        print("talking..........")

    def sleep(self,name):
        print("i am a method")
        print("sleep", name)

    def walk(self):
        print("i am walking")

    def walk1(self):
        return ("i am walking")

    def dance(self,name):
        print("i can dance",name)
        return "i am a dancer"



# create an object


sand = person()
sand.name = "sand"
sand.walk()
dhya =person()
dhya.name = "dhya"
dhya.talk()

