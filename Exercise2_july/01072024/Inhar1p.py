# single inheritance

class parent:
    gold = "2kg"
    def BHK2(self):
        print('BHK2')

class child(parent):
    def BHK3(self):
        print('BHK3')

child_obj = child()
child_obj.BHK2()
child_obj.BHK3()
print(child_obj.gold)