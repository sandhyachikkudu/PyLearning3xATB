class car:
    def __init__(self):
        self.public_var="public"
        self.__protected_var = "protected123"
        self._private_var="pass@123"

    def private_method(self):
        print("protected")

    def printname(self):
        if self.public_var == "protected123":
            print("hi,123")

        print("i am allowed,public")




alto = car()
alto.printname()



