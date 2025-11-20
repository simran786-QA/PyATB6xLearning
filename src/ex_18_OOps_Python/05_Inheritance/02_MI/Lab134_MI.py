# -------------------------------------------------------------
# Step 1: Create Base Classes
# -------------------------------------------------------------
class APIBase:
    def api_auth(self):
        print("Authenticating API")


class DBBase:
    def db_connect(self):
        print("Connecting to the DB")


# -------------------------------------------------------------
# Step 2: Create Hybrid Class Using Multiple Inheritance
# -------------------------------------------------------------
class TestHybrid(APIBase, DBBase):
    def run(self):
        self.api_auth()     # Calling API authentication
        self.db_connect()   # Calling DB connection
        print("Test Case Running.")


# -------------------------------------------------------------
# Step 3: Create Object & Execute Test
# -------------------------------------------------------------
tc1 = TestHybrid()
tc1.run()


# -------------------------------------------------------------
# Summary
# -------------------------------------------------------------
# - Demonstrated multiple inheritance in Python.
# - TestHybrid inherits features from APIBase and DBBase.
# - run() method calls both parent class functionalities.
# - Useful for API + Database combined test scenarios.


# -------------------------------------------------------------
# Commit Message
# -------------------------------------------------------------
# feat: added hybrid test class using multiple inheritance
# - Added APIBase and DBBase classes
# - Created TestHybrid to combine both functionalities
# - Tested authentication + DB connection flow
