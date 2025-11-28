# -------------------------------------------------------------
# Step 1: Define First Decorator
# -------------------------------------------------------------
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper


# -------------------------------------------------------------
# Step 2: Define Second Decorator (Not Used Here)
# -------------------------------------------------------------
def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


# -------------------------------------------------------------
# Step 3: Apply Decorators to Function
# -------------------------------------------------------------
@decorator1
@decorator1
def say_hello():
    print("Hello!")


# -------------------------------------------------------------
# Step 4: Execute Function
# -------------------------------------------------------------
say_hello()
