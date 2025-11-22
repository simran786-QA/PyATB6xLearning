# -------------------------------------------------------------
# Step 1: TestSuite Base Class
# -------------------------------------------------------------
class TestSuite:
    def info(self):
        print("Test suite information")


# -------------------------------------------------------------
# Step 2: BaseTest Inheriting from TestSuite
# -------------------------------------------------------------
class BaseTest(TestSuite):
    def setup(self):
        print("Base setup")

    def run(self):      # Parent method
        print("Base test execution")


# -------------------------------------------------------------
# Step 3: LoginTest Overrides run()
# -------------------------------------------------------------
class LoginTest(BaseTest):
    def run(self):      # overriding
        print("Login test execution")


# -------------------------------------------------------------
# Step 4: APITest Overrides run()
# -------------------------------------------------------------
class APITest(BaseTest):
    def run(self):      # overriding
        print("API test execution")


# -------------------------------------------------------------
# Step 5: Create Object & Execute run()
# -------------------------------------------------------------
# t = LoginTest()   # Uncomment to test login behavior
# t = APITest()     # Uncomment to test API behavior
t = BaseTest()       # Using parent class
t.run()              # Output: Base test execution


# -------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------
# - TestSuite → parent class with info()
# - BaseTest → extends TestSuite, adds setup() and run()
# - LoginTest → overrides run() with Login-specific behavior
# - APITest   → overrides run() with API-specific behavior
# - Object type decides which run() is executed (method overriding)

