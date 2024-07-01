class VWLogin:

    def __init__(self,email,password,username):
        self.__username = username
        self.__password = password
        self.__email =email

    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password == "pass123":
            print("Login successful!")

        else:
            print("Login failed!")



page1=VWLogin("abc@gmail.com", "pass123","sand")
page1.login_confirm()