# hierarchical inheritance

class father:
    gold = "3kg"
    def BHK1(self):
        print("BHK1")


class sravs(father):
    def BHK2(self):
        print("BHK2")

class swathi(father):
    def BHK3(self):
        print("BHK3")

class sand(father):
    def BHK4(self):
        print("BHK4")



s1 = sravs()
s1.BHK2()
s1.BHK1()
print(s1.gold)
s2 = sand()
s2.BHK4()
s2.BHK1()
print(s2.gold)

s3 = swathi()
s3.BHK3()
s3.BHK1()
print(s3.gold)
