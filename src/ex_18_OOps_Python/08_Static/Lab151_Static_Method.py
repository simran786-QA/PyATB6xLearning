# ---------------------------------------------
# TestCounter – Object Creation Counter Example
# ---------------------------------------------

class TestCounter:
    count = 0   # Class variable shared by all objects

    def __init__(self):
        # Each time object is created, count is increased
        TestCounter.count += 1


# Creating multiple objects (test cases simulation)
t1 = TestCounter()
t2 = TestCounter()
t3 = TestCounter()

# Display total number of times object was created
print("Total Objects Created:", TestCounter.count)

"""
EXPLANATION (HINDI + ENGLISH):

1. class TestCounter:
   - Ek class banayi jisme ek class variable 'count' rakha.
   - This variable is shared across ALL objects.

2. def __init__(self):
   - Jab bhi new object banega, constructor execute hoga.
   - count += 1 se total object creation count badh jayega.

3. t1, t2, t3:
   - Teen objects ban rahe hain, so count = 3.

REAL QA USE:
- Aise class counters automation frameworks mein use hote hain:
  - test execution count
  - pass/fail counters
  - how many tests ran
  - how many retries happened
"""

# ---------------------------------------------
# END OF ONE COMBINED CODE
# ---------------------------------------------
