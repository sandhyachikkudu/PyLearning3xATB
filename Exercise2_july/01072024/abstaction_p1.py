from abc import ABC, abstractmethod
class animal(ABC):

    def __init__(self,name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass


class cat(animal):
    def sound(self):
        return 'meow'

class dog(animal):
    def sound(self):
        return 'bowbow!'


d = dog("DOG")
print(d.sound())

c=cat("CAT")
print(c.sound())