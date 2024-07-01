class person:
    # class variables/instance variable
    name = "sand"
    age = None

    def walk(self):
        age = 10
        print("i am method")
        print("hi", self.age)


s = person()
s.walk()


class car:
    name = None
    make = None
    model = None
    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model


    def start_engine(self):
        print("starting the ca with name:"+self.name)
        print("starting the ca with make:"+self.make)
        print("starting the ca with model:"+self.model)


lambo = car("Lambo","v2","2023")

lambo.start_engine()

activa = car("Activa","v3","2024")
activa.start_engine()



class VWOlogin:
    email = None
    password = None

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "sand@gamail.com" and self.password == "pass123":
            print("Login successful")
        # if self.password == "pass123":
        #     print("Welcome to VWOlogin")
        else:
            print("not allowed")


# amit = VWOlogin("amit@12gamail.com", "pass123")
# amit.login_confirm()
#
# pro = VWOlogin("pro123@gmail.com", "lass123")
# pro.login_confirm()


email = input("Enter your email: ")
password = input("Enter your password: ")
sand = VWOlogin(email, password)
sand.login_confirm()

email = input("Enter your email: ")
password = input("Enter your password: ")
san = VWOlogin(email, password)
san.login_confirm()
