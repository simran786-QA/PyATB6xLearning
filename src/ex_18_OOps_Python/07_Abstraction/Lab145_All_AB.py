# Abstraction
# Hide the details and show what is required.

# Car - with key _ __private, tyres -> public,

# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox?
#===============================================

# Abstraction Example in Python

# 👉 Abstraction hides complex internal logic and exposes only essential features.
# 👉 Achieved using Abstract Base Classes (ABC) and @abstractmethod.

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        """Each animal must define its own sound."""
        pass


class Dog(Animal):
    def sound(self):
        print("Bark")


# Object creation
dog = Dog("PP")
dog.sound()
