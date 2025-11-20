# -------------------------------------------------------------
# Step 1: Create Base Class
# -------------------------------------------------------------
class BaseTest:
    def run(self):
        print("Running generic test")


# -------------------------------------------------------------
# Step 2: Create Child Class That Overrides Parent Method
# -------------------------------------------------------------
class LoginTest(BaseTest):

    def run(self):
        print("Running Login Test")


# -------------------------------------------------------------
# Step 3: Create Object & Run the Method
# -------------------------------------------------------------
# t = LoginTest()   # If you want child class behavior
t = BaseTest()       # Calls Base class method
t.run()              # Output → Running generic test


# -------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------
# - BaseTest has a run() method.
# - LoginTest overrides run().
# - Object of BaseTest → calls BaseTest.run()
# - If LoginTest object is used → it will call overridden method.


# -------------------------------------------------------------
# COMMIT MESSAGE
# -------------------------------------------------------------
# feat: added method overriding example using BaseTest and LoginTest classes
# - Demonstrates inheritance and overriding
# - Shows how object type decides which run() is executed
