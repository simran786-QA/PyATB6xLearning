```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python List – Introduction and Basic Operations
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Understanding List
# -------------------------------------------------------------
# A list is a collection of multiple items.
# Lists can store same or different data types.

# grocery List - butter, bread, banana, paneer.
# 10th marks - 90, 91, 92, 78, 56


# -------------------------------------------------------------
# Step 2: Create lists
# -------------------------------------------------------------
# my_list contains same type of data (integers).
# my_list2 contains multiple data types.

my_list = [1, 2, 3]
my_list2 = [1, True, "Pramod", 12.34]


# -------------------------------------------------------------
# Step 3: Print list and its type
# -------------------------------------------------------------
# type() shows the datatype of the variable.

print(my_list)
print(type(my_list))   # <class 'list'>


# -------------------------------------------------------------
# Step 4: Find length of list
# -------------------------------------------------------------
# len() returns total number of elements.

print(len(my_list))


# -------------------------------------------------------------
# Step 5: Access list elements using index
# -------------------------------------------------------------
# Index starts from 0 in Python.

print(my_list[0])
print(my_list[2])


# -------------------------------------------------------------
# Step 6: Invalid index example (commented)
# -------------------------------------------------------------
# Accessing an index that does not exist
# will raise IndexError.

# print(my_list[6])  # IndexError: list index out of range


# -------------------------------------------------------------
# Hindi Explanation:
# - List ek collection hota hai jisme multiple values store hoti hain.
# - List me same ya different data types store ho sakte hain.
# - Indexing 0 se start hoti hai.
# - len() list ke total elements count karta hai.
# - Invalid index access karne par IndexError aata hai.
#
# English Explanation:
# - A list stores multiple values together.
# - Lists can contain same or mixed data types.
# - Indexing starts from 0 in Python.
# - len() returns the total number of elements.
# - Accessing an invalid index raises IndexError.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lists are ordered collections in Python.
# 2. Lists support indexing and multiple data types.
# 3. len() gives total element count.
# 4. Invalid index access causes IndexError.
# -------------------------------------------------------------
```
