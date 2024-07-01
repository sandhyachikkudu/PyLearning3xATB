from abc import ABC, abstractmethod
class Pythom3x(ABC):
    @abstractmethod
    def payfee(self):
        pass


    def enrolled(self):
        print("enrolled")


class sandhya(Pythom3x):
    def payfee(self):
        print("paidfee ")

sandhya = sandhya()
sandhya.enrolled()

