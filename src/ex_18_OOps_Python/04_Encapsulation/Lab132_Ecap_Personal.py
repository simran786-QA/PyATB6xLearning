class Home:
    def __init__(self):
        self.public_var = "father"                 # Public
        self._protected_var = "brother"            # Protected
        self.__private__var_dadsa__dasda__ = "baby"  # Private variable

    def mom(self):
        # Correct way to access private variable inside class
        print(self.__private__var_dadsa__dasda__)
        self.__wife()

    def __wife(self):   # Private method
        print("Private Wife")


# Object creation
object_ref = Home()

# Accessing private members directly will fail
# object_ref.__wife()      # ❌ Not allowed
# object_ref.__private_var # ❌ Not allowed

object_ref.mom()

# print(object_ref._protected_var)  # ⚠️ Accessible but not recommended
