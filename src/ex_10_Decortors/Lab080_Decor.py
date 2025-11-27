# -------------------------------------------------------------
# Step 1: Create Decorator - before_after_ui_test
# -------------------------------------------------------------

def before_after_ui_test(func):
    def wrapper():
        print("Before Running UI Code")
        func()
        print("After Running UI Code")
    return wrapper   # FIXED ✔ return wrapper, not wrapper()


# -------------------------------------------------------------
# Step 2: Apply Decorator
# -------------------------------------------------------------

@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI Test")


# -------------------------------------------------------------
# Step 3: Execute Test
# -------------------------------------------------------------
test_ui()
