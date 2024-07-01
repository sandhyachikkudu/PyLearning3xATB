from abc import ABC, abstractmethod
class ATB(ABC):
    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass


class student(ATB):
    def perform_task1(self):
        return 'task done1'

    def perform_task2(self):
        return 'task done2'


sand = student()
print(sand.perform_task1())
print(sand.perform_task2())

