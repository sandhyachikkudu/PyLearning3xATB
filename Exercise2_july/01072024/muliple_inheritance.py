class father:
    def father_money(self):
        return "father's money:5"
    def home_money(self):
        return "money from father"

class mother:
    def mother_money(self):
        return "mother's money:10"
    def home_money(self):
        return "money from mother"
class child(father, mother):
    def home_money(self):
        return "money from child"

son = child()
print(son.home_money())
print(son.mother_money())
print(son.father_money())