# parent class,base class
class grandparent:
    key="abc"
    def grandparent(self):
        return "grandparent method"

# sub class,child class
class parent(grandparent):
    def parent(self):
        return "parent method"

person = parent()
print(person.parent())
print(person.grandparent())
print(person.key)