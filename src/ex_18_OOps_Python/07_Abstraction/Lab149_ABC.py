# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Abstraction + Multi-Level Inheritance (Excel + Browser)
# -------------------------------------------------------------

# Step 1: Import Required Modules
from abc import ABC, abstractmethod

# -------------------------------------------------------------
# Step 2: Base Abstract Class - ExcelReader
class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass
    # Hindi:
    # Har test class ko Excel se data read karna hoga.
    #
    # English:
    # Every test class must implement Excel data reading.

# -------------------------------------------------------------
# Step 3: Abstract Browser Class (inherits ExcelReader)
class Browser(ExcelReader):

    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass
    # Hindi:
    # Browser class base structure define karti hai – har test ko
    # startBrowser() aur stopBrowser() implement karna hi padega.
    #
    # English:
    # Browser class forces every child class to implement
    # startBrowser() and stopBrowser().

# -------------------------------------------------------------
# Step 4: Concrete Test Class Implementing Everything
class TC1(Browser):

    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()
    # Hindi:
    # TC1 class complete implementation deti hai aur runTc()
    # poora flow chalata hai.
    #
    # English:
    # TC1 provides full implementation & runTc() executes the flow.

# -------------------------------------------------------------
# Step 5: Run Test Case
tc1 = TC1()
tc1.runTc()

# -------------------------------------------------------------
# Summary
# 1. ExcelReader → Abstract class for Excel operations.
# 2. Browser → Abstract class extending ExcelReader.
# 3. TC1 → Concrete class implementing all abstract methods.
# 4. runTc() → Defines real automation workflow.
# 5. Demonstrates Abstraction + Multi-Level Inheritance.
# -------------------------------------------------------------
