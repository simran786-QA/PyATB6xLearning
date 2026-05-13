```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Tuple – Introduction and Basic Operations
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create a tuple
# -------------------------------------------------------------
# Tuple is an ordered collection of items.
# Tuples are immutable (cannot be modified).

my_tuple = (1, 2, 3)

print(my_tuple)


# -------------------------------------------------------------
# Step 2: Tuple immutability example
# -------------------------------------------------------------
# Tuple elements cannot be changed after creation.

# my_tuple[0] = 12
# TypeError: 'tuple' object does not support item assignment


# -------------------------------------------------------------
# Step 3: Tuple with mixed data types
# -------------------------------------------------------------
# Tuples can store different types of data together.

info = ("Pramod", 34, True, 9.8)

print(info)


# -------------------------------------------------------------
# Step 4: Tuple with one element
# -------------------------------------------------------------
# A comma is required for single-element tuple.

single = (3,)

print(type(single))   # <class 'tuple'>


# -------------------------------------------------------------
# Hindi Explanation:
# - Tuple ek ordered collection hota hai.
# - Tuple immutable hota hai, yani values change nahi kar sakte.
# - Different data types ek tuple me store ho sakte hain.
# - Single element tuple banane ke liye comma zaruri hota hai.
# - Agar comma nahi lagaya, to Python usse normal integer maanega.
#
# English Explanation:
# - A tuple is an ordered collection in Python.
# - Tuples are immutable, so elements cannot be modified.
# - Mixed data types can be stored in a tuple.
# - A comma is mandatory for a single-element tuple.
# - Without the comma, Python treats it as a normal integer.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Tuples are ordered and immutable collections.
# 2. Tuple elements cannot be updated after creation.
# 3. Tuples support mixed data types.
# 4. Single-element tuples require a trailing comma.
# -------------------------------------------------------------
```
