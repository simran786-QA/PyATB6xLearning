# -------------------------------------------------------------
# Step 1: Define a Function Returning Multiple Values
# -------------------------------------------------------------
def math_operations(a, b):
    return a + b, a - b, a * b


# -------------------------------------------------------------
# Step 2: Call the Function & Unpack Results
# -------------------------------------------------------------
sum_result, diff_result, mul_result = math_operations(3, 4)


# -------------------------------------------------------------
# Step 3: Print All Results
# -------------------------------------------------------------
print(sum_result)
print(diff_result)
print(mul_result)
