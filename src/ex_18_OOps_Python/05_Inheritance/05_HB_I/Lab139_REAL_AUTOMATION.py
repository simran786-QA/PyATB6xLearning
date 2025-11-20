# -------------------------------------------------------------
# Concept: Constructor with Inheritance (Single Inheritance)
# -------------------------------------------------------------
# - BaseTest has a constructor (__init__) that accepts browser.
# - LoginTest and SignupTest inherit this constructor.
# - Each subclass overrides run_test() to perform specific actions.


# -------------------------------------------------------------
# Step 1: Create Base Class with Constructor
# -------------------------------------------------------------
class BaseTest:
    def __init__(self, broswer):
        self.browser = broswer

    def setup(self):
        print(f"Launching {self.browser}")


# -------------------------------------------------------------
# Step 2: Create Child Classes (Single Inheritance)
# -------------------------------------------------------------
class LoginTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running login test...")


class SignupTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running signup test...")


# -------------------------------------------------------------
# Step 3: Create Objects & Run Tests
# -------------------------------------------------------------
t = LoginTest("chrome")
t.run_test()

t = LoginTest("firefox")
t.run_test()


# -------------------------------------------------------------
# Expected Output
# -------------------------------------------------------------
# Launching chrome
# Running login test...
#
# Launching firefox
# Running login test...


# -------------------------------------------------------------
# Summary
# -------------------------------------------------------------
# - Demonstrated single inheritance with constructor reuse.
# - BaseTest handles the browser setup.
# - Child classes (LoginTest, SignupTest) use inherited setup()
#   and implement their own test logic in run_test().
# - Shows how browser configuration can be reused across tests.


# -------------------------------------------------------------
# Commit Message
# -------------------------------------------------------------
# feat: added single inheritance example with constructor reuse
# - BaseTest defines reusable browser setup
# - LoginTest/SignupTest implement specific test flows
