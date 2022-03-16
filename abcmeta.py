from abc import ABCMeta, abstractmethod


class Family(metaclass=ABCMeta):
    @abstractmethod
    def get_dad(self):
        """Any extension of the Family class must implement a `get_dad` method"""


class MyFamily(Family):
    pass


class MyFamily(Family):
    def get_dad(self):
        return "Me"
