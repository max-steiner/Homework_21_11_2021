from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def __init__(self, _id, name, address, age):
        self._id = _id
        self.name = name
        self.address = address
        self.age = age

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def __str__(self):
        return f'--------\n' \
               f'[Employee]:\n' \
               f'Name - {self.name}\n'\
               f'id - {self._id}\n'\
               f'Address - {self.address}\n'\
               f'Age - {self.age}\n' \
               f'__________________'
