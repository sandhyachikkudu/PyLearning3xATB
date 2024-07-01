class password:
    def __init__(self, password):
        self.__password = password
        self.public_var=10

    def get_password(self,is_auth):
        if is_auth:
            print(self.__password)

        else:
            print("invalid password")

    def set_password(self,password):
        if len(password) > 8:
            self.__password = password
            print("your password:",self.__password)
        else:
            print("invalid password,weak")


pwd = password("lasadasf")
pwd.set_password("sand@20000")
pwd.get_password(True)





