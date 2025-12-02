from abc import ABC, abstractmethod

# Abstract class (Rule/Blueprint)
class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass  # No implementation here (hidden details)


# Child class (Actual implementation)
class Amit(Father):

    def loan(self):
        print(f"{self.name} is giving a loan of 50,000 INR")


# Object of child class
amit = Amit("Amit Sharma")
amit.loan()
