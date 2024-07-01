class grandparent:
    def grandparent_method(self):
        print("grandparent method called")

class parnet(grandparent):
    def parnet_method(self):
        print("parnet method called")

class child(parnet):
    def child_method(self):
        print("child method called")


child_ref= child()
child_ref.grandparent_method()
child_ref.parnet_method()
child_ref.child_method()
print("--------------")

parent =parnet()
parent.grandparent_method()
parent.parnet_method()
print("--------------")

grandparent = grandparent()
grandparent.grandparent_method()
