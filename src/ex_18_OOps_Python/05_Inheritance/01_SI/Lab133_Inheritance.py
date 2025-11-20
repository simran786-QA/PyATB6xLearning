# -------------------------------------------------------------
# Step 1: Parent Class (Base Class)
# -------------------------------------------------------------
class BaseTest:
    driver = "Chrome"           # Public
    __driver2 = "FF"            # Private

    def setup(self):
        print("Base setup with the browser and env " + self.__driver2)


# -------------------------------------------------------------
# Step 2: Child Class (Derived Class)
# -------------------------------------------------------------
class LoginTest(BaseTest):
    def run(self):
        self.setup()            # Calling parent method
        print("Running the Testcases -> " + self.driver)


# -------------------------------------------------------------
# Step 3: Create Object and Execute
# -------------------------------------------------------------
t = LoginTest()
t.run()
