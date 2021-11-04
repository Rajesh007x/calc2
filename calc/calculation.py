"""This is our calculation base class / Abstract Class"""
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
class Calculation:
    #contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class
        # pylint: disable=line-too-long
        #these are instance properties that are being sharred with the child classes (addition, subtraction, etc...)
        self.value_a = value_a
        self.value_b = value_b
    # Class Factory Method <- bound to the class and not the instance of the class
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)
