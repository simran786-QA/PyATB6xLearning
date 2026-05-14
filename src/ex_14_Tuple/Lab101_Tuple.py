# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Tuple – Operations, Methods, and Conversion
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create a tuple of cities
# -------------------------------------------------------------
# Tuple stores multiple city names.

cities = ("London", "Paris", "Los Angeles", "Tokyo")


# -------------------------------------------------------------
# Step 2: Tuple operations
# -------------------------------------------------------------
# len() returns total elements.
# in keyword checks existence of an item.

print(len(cities))

print("Paris" in cities)
print("New Delhi" in cities)


# -------------------------------------------------------------
# Step 3: Tuple immutability example
# -------------------------------------------------------------
# Tuples do not support append() because they are immutable.

t = (12, 34, 56)

# t.append(12)
# AttributeError: 'tuple' object has no attribute 'append'


# -------------------------------------------------------------
# Step 4: Convert list to tuple
# -------------------------------------------------------------
# tuple() converts list into tuple.

ENV_API_URLS = tuple([
    "abc.com/get",
    "xyz.com/post",
    "qwe.com/put"
])

print(ENV_API_URLS)


# -------------------------------------------------------------
# Step 5: Iterate through tuple
# -------------------------------------------------------------
# for loop accesses each element one by one.

colors = ("red", "green", "blue")

for c in colors:
    print(c)


# -------------------------------------------------------------
# Step 6: Tuple and string repetition
# -------------------------------------------------------------
# * operator repeats values multiple times.

numbers = "Pramod" * 3
print(numbers)

numbers = (1, 2) * 3
print(numbers)

print(" ---------")


# -------------------------------------------------------------
# Step 7: Tuple methods
# -------------------------------------------------------------
# count() counts occurrences.
# index() returns position of element.

nums = (1, 2, 2, 3, 2)

print(len(nums))
print(nums.count(2))
print(nums.index(3))


# -------------------------------------------------------------
# Step 8: List to tuple conversion
# -------------------------------------------------------------
# tuple() converts list into tuple.

my_list = [1, 2, 3]

my_tuple = tuple(my_list)

print(my_tuple)    # (1, 2, 3)


# -------------------------------------------------------------
# Step 9: Tuple to list conversion
# -------------------------------------------------------------
# list() converts tuple back into list.

back_to_list = list(my_tuple)

print(back_to_list)   # [1, 2, 3]

print(max(back_to_list))


# -------------------------------------------------------------
# Step 10: List slicing and negative indexing
# -------------------------------------------------------------
# Slicing extracts elements from a range.
# Negative index accesses elements from the end.

my_list = [1, 2, 3]

print(my_list[0:2])

print(my_list[-1])


# -------------------------------------------------------------
# Hindi Explanation:
# - len() tuple ke total elements count karta hai.
# - in keyword check karta hai ki element exist karta hai ya nahi.
# - Tuple immutable hota hai, isliye append() use nahi kar sakte.
# - tuple() aur list() conversion ke liye use hote hain.
# - for loop tuple ke elements iterate karta hai.
# - * operator values ko repeat karta hai.
# - count() occurrences count karta hai.
# - index() element ka position return karta hai.
# - Slicing specific range ke elements deta hai.
# - Negative indexing last se elements access karti hai.
#
# English Explanation:
# - len() returns total elements in tuple.
# - in keyword checks item existence.
# - Tuples are immutable, so append() is not supported.
# - tuple() and list() are used for conversion.
# - for loop iterates through tuple elements.
# - * operator repeats values.
# - count() returns frequency of an element.
# - index() gives element position.
# - Slicing extracts a range of elements.
# - Negative indexing accesses elements from the end.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Tuples are immutable collections.
# 2. Tuples support methods like count() and index().
# 3. Conversion between list and tuple is possible.
# 4. Slicing and negative indexing help access data.
# 5. * operator repeats tuple or string values.
# -------------------------------------------------------------