class GF:
    def car(self):
        print("Old Car")

class F(GF):
    def car(self):
        print("used Car")
class S(F):
    def car(self):
        print("new Car")

son = S()
son.car()



class GF:
    def car(self):
        print("Old Car")

class F(GF):
   pass
class S(F):
    pass

son1 = S()
son1.car()
