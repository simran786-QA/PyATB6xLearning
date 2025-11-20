# -------------------------------------------------------------
# Concept: Multi-Level Inheritance in Python
# -------------------------------------------------------------
# Multi-level inheritance means a class inherits from another class,
# which itself inherits from another class.
# Chain: TestSuite → BaseTest → UITest


# -------------------------------------------------------------
# Step 1: Grandparent Class
# -------------------------------------------------------------
class TestSuite:
    def info(self):
        print("This is GF - Step 1")


# -------------------------------------------------------------
# Step 2: Parent Class (inherits from TestSuite)
# -------------------------------------------------------------
class BaseTest(TestSuite):
    def setup(self):
        print("BaseTest - F - Step 2")


# -------------------------------------------------------------
# Step 3: Child Class (inherits from BaseTest)
# -------------------------------------------------------------
class UITest(BaseTest):
    def run(self):
        self.info()      # From TestSuite
        self.setup()     # From BaseTest
        print("Running Test Case")


# -------------------------------------------------------------
# Step 4: Create Object & Execute
# -------------------------------------------------------------
test = UITest()
test.run()


# -------------------------------------------------------------
# Output
# -------------------------------------------------------------
# This is GF - Step 1
# BaseTest - F - Step 2
# Running Test Case


# -------------------------------------------------------------
# Summary
# -------------------------------------------------------------
# - Demonstrates multi-level inheritance (3 levels).
# - UITest inherits behavior from BaseTest and TestSuite.
# - Child class has access to methods from all ancestor classes.
# - Shows how method calls propagate through inheritance chain.


# -------------------------------------------------------------
# Commit Message
# -------------------------------------------------------------
# feat: added multi-level inheritance example (TestSuite → BaseTest → UITest)
# - Implemented method chaining using inherited functions
# - Demonstrated hierarchical execution flow
