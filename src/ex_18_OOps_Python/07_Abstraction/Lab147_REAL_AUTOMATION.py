# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Abstraction using ABC – Browser Manager Example
# -------------------------------------------------------------

# Step 1: Import Required Module (ABC + abstractmethod)
from abc import ABC, abstractmethod

# -------------------------------------------------------------
# Step 2: Create an Abstract Class
class BrowserManger(ABC):

    @abstractmethod
    def start(self):
        pass
    # Hindi:
    # start() ek abstract method hai — iski body nahi hoti.
    # Har browser class ko ise implement karna hoga.
    #
    # English:
    # start() is an abstract method — it must be implemented
    # by every child browser class.

    def stop(self):
        print("Stop command, common")
    # Hindi:
    # stop() normal method hai, sab browsers use kar sakte hain.
    #
    # English:
    # stop() is a regular method that every browser class inherits.

# -------------------------------------------------------------
# Step 3: Create Child Class & Implement Abstract Method
class ChromeBrowser(BrowserManger):

    def start(self):
        # Example → t = ChromeDriver()
        print("We are starting the chrome")
    # Hindi:
    # Yahan abstract method ki real implementation di gayi hai.
    #
    # English:
    # Here we provide the actual implementation of start().

# -------------------------------------------------------------
# Step 4: Create Object & Execute Methods
tc = ChromeBrowser()
tc.start()
tc.stop()

# -------------------------------------------------------------
# Step 5: Summary
# 1. Abstract class ensures structure (BrowserManger).
# 2. Child class must implement abstract method (start()).
# 3. stop() is inherited by all child classes.
# 4. Abstraction hides details & provides clean architecture.
# -------------------------------------------------------------

