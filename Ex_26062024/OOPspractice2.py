class calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mult(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

    def remain(self):
        return self.a%self.b





s = calc(5,3)
print(s.sum())
print(s.sub())
print(s.mult())
print(s.div())
print(s.remain())







