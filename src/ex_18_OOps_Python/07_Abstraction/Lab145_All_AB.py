# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Abstraction using ABC (Abstract Base Class)
# -------------------------------------------------------------

# Step 1: Import Required Module
from abc import ABC, abstractmethod

# -------------------------------------------------------------
# Step 2: Create an Abstract Class
class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass
    # Hindi:
    # loan() ek abstract method hai. Iski koi body nahi hoti.
    # Har child class ko ise implement karna zaroori hai.
    #
    # English:
    # loan() is an abstract method. It has no body.
    # Every subclass MUST implement this method.

# -------------------------------------------------------------
# Step 3: Create a Child Class That Implements the Abstract Method
class Amit(Father):

    def loan(self):
        print("Giving the 50K loan")
    # Hindi:
    # Abstract method yahan override kiya gaya hai.
    #
    # English:
    # Abstract method is overridden here.

# -------------------------------------------------------------
# Step 4: Create Object and Call Implemented Method
amit = Amit("AMIT SHARMA")
amit.loan()

# -------------------------------------------------------------
# Step 5: Summary
# 1. Abstract class = Blueprint, cannot be instantiated.
# 2. Abstract method = Must be implemented by child class.
# 3. @abstractmethod enforces structure.
# 4. Father class contains rule.
# 5. Amit class provides real implementation.
# -------------------------------------------------------------
