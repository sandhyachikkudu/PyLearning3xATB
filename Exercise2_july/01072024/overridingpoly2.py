class father:
    def home(self):
        print("3bhk")

class son(father):
    def home(self):
        super().home()
        print("no house")


pramod = son()
pramod.home()