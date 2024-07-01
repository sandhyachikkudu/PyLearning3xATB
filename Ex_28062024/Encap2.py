class myclass:
    def __init__(self):
        self.name = "amit"

    def public_function(self):
        print("public function called")

    def __private_function(self):
        print("private function called")

    def public_fn_private_function(self):
        self.__private_function()

a= myclass()
a.public_fn_private_function()
a.public_function()