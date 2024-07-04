# hybrid inheritance

# multiple types of inheritance
# such as single,multilevel,multiple and hierarchical

class A:
    def methodA(self):
        print('method A')

class B(A):
    def methodB(self):
        print('method B')

class C(A):
    def methodC(self):
        print('method C')

class D(B,C):
    # multilevel,multiple ----->MRo--method resolution model---who ever is first t=that will execute
    def methodD(self):
        print('method D')


d = D()
d.methodD()
d.methodC()
d.methodB()
d.methodA()
