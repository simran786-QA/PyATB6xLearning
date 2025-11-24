# ======================================================
# Test Execution Counter + Sample Tests (Runnable Code)
# ======================================================

import datetime


class TestExecutionCounter:
    def __init__(self):
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.history = []

    def start_test(self, test_name):
        self.total += 1
        entry = {
            "test_name": test_name,
            "start_time": datetime.datetime.now(),
            "status": None,
            "end_time": None
        }
        self.history.append(entry)
        print(f"[START] {test_name}")

    def end_test(self, test_name, status):
        entry = next(x for x in self.history if x["test_name"] == test_name and x["status"] is None)
        entry["status"] = status
        entry["end_time"] = datetime.datetime.now()

        if status == "PASS":
            self.passed += 1
        elif status == "FAIL":
            self.failed += 1
        elif status == "SKIPPED":
            self.skipped += 1

        print(f"[END] {test_name} → {status}")

    def summary(self):
        print("\n===== TEST EXECUTION SUMMARY =====")
        print(f"Total Tests : {self.total}")
        print(f"Passed      : {self.passed}")
        print(f"Failed      : {self.failed}")
        print(f"Skipped     : {self.skipped}")
        print("=================================\n")


# ===============================
# Base Test + Sample Tests
# ===============================

class BaseTest:
    def __init__(self, name, counter: TestExecutionCounter):
        self.name = name
        self.counter = counter

    def setup(self):
        print("Setting up test environment...")

    def run(self):
        raise NotImplementedError("Child class must override run()")


class LoginTest(BaseTest):
    def run(self):
        self.counter.start_test(self.name)
        self.setup()
        print("Running Login Test Steps...")
        # Simulate success
        self.counter.end_test(self.name, "PASS")


class APITest(BaseTest):
    def run(self):
        self.counter.start_test(self.name)
        self.setup()
        print("Running API Test Steps...")
        # Simulate failure
        self.counter.end_test(self.name, "FAIL")


class SkipTest(BaseTest):
    def run(self):
        self.counter.start_test(self.name)
        print("Skipping test...")
        self.counter.end_test(self.name, "SKIPPED")


# ===============================
# Run All Tests
# ===============================

if __name__ == "__main__":
    counter = TestExecutionCounter()

    tests = [
        LoginTest("Login Test", counter),
        APITest("API Test", counter),
        SkipTest("Skipped Test", counter)
    ]

    for test in tests:
        test.run()

    counter.summary()
