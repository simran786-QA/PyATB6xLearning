# -------------------------------------------------------------
# Step 1: Import Required Modules
# -------------------------------------------------------------
import time


# -------------------------------------------------------------
# Step 2: Create Decorator to Print Logs
# -------------------------------------------------------------
def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the log")
    return wrapper


# -------------------------------------------------------------
# Step 3: Create Decorator to Track Execution Time
# -------------------------------------------------------------
def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total Time Take by Func -> ", end_time - start_time)
    return wrapper


# -------------------------------------------------------------
# Step 4: Test Case 1 (UI Test 1)
# -------------------------------------------------------------
@time_decorator
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)


# -------------------------------------------------------------
# Step 5: Test Case 2 (UI Test 2)
# -------------------------------------------------------------
@time_decorator
@print_logs
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)


# -------------------------------------------------------------
# Step 6: Execute the Test Cases
# -------------------------------------------------------------
test_ui_1()
test_ui_2()
