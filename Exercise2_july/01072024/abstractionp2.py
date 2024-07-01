from abc import ABC, abstractmethod
class father(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

# class pramod(father):
#     pass
#
#
# son = pramod("pamo")
# print(son.loan())----TypeError: Can't instantiate
# abstract class pramod without an implementation for abstract method 'loan'

class son(father):
    def loan(self):
        print("loan given")


son = son("pramod")
son.loan()

