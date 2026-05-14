```python id="w2m8r1"
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Tuple and List – Conversion and Nested Tuples
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Modify list elements
# -------------------------------------------------------------
# Lists are mutable, so elements can be changed.

shopping_list_wife = ["bread", "butter", "paneer"]

shopping_list_wife[2] = "milk"

print(shopping_list_wife)


# -------------------------------------------------------------
# Step 2: Tuple example
# -------------------------------------------------------------
# Tuples are immutable collections.

my_tuple = ("tta.com", "sdet.live")

print(my_tuple)


# -------------------------------------------------------------
# Step 3: Convert tuple to list
# -------------------------------------------------------------
# Conversion is useful when modification is required.

my_api_list = list(my_tuple)

my_api_list.append("item2")


# -------------------------------------------------------------
# Step 4: Convert list back to tuple
# -------------------------------------------------------------
# After modification, list is converted again into tuple.

my_api_list2 = tuple(my_api_list)

print(my_api_list2)


# -------------------------------------------------------------
# Step 5: Real use case of tuples
# -------------------------------------------------------------
# API URLs are fixed values, so tuple is suitable.

API_URLSs = (
    "https://sdet.live/python0x",
    "https://awesomeqa.com",
    "https://thetestingacademy.com"
)

print(API_URLSs[0])
print(API_URLSs[1])


# -------------------------------------------------------------
# Step 6: Create empty tuple and list
# -------------------------------------------------------------
# tuple() creates empty tuple.
# list() creates empty list.

t = tuple()
print(t)

l = list()
print(l)


# -------------------------------------------------------------
# Step 7: Convert list to tuple
# -------------------------------------------------------------
# tuple() converts list into tuple.

t1 = tuple(["pramod", "amit", "manisha"])

print(t1)


# -------------------------------------------------------------
# Step 8: Nested tuple example
# -------------------------------------------------------------
# Tuples can contain other tuples.

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")

new_tuple = (hero1, hero2)

print(new_tuple)


# -------------------------------------------------------------
# Step 9: Access nested tuple elements
# -------------------------------------------------------------
# Multiple indexing is used for nested tuples.

print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])


# -------------------------------------------------------------
# Hindi Explanation:
# - Lists mutable hoti hain, isliye values change kar sakte hain.
# - Tuples immutable hote hain, values directly modify nahi hoti.
# - Tuple ko list me convert karke changes kar sakte hain.
# - Modified list ko dobara tuple me convert kiya ja sakta hai.
# - API URLs jaise fixed data ke liye tuples useful hote hain.
# - Nested tuples me tuple ke andar tuple hota hai.
# - Nested elements access karne ke liye multiple indexing use hoti hai.
#
# English Explanation:
# - Lists are mutable, so elements can be updated.
# - Tuples are immutable and cannot be modified directly.
# - Tuples can be converted into lists for modification.
# - Lists can be converted back into tuples.
# - Tuples are useful for fixed data like API URLs.
# - Nested tuples contain tuples inside tuples.
# - Multiple indexing is used to access nested elements.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lists are mutable; tuples are immutable.
# 2. tuple() and list() help in conversion.
# 3. Tuples are ideal for fixed data storage.
# 4. Nested tuples support multidimensional structures.
# 5. Multiple indexing accesses nested tuple values.
# -------------------------------------------------------------
```
