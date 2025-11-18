# Encapsulation -
# Hiding data members using private variables + methods

class Car:
    def __init__(self):
        self.public_pramod = "pramod"            # Public variable
        self.__private_baby = "pass123"          # Private variable

    def nany(self):
        self.__password_yogesh_private = "345"   # Private variable created inside method


# Object creation
object_ref = Car()

print(object_ref.public_pramod)   # Accessible
# print(object_ref.__private_baby)  # ❌ Not accessible (private)

object_ref.nany()
