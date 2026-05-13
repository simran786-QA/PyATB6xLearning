```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python List – Update, Loop, and List Methods
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create and update list elements
# -------------------------------------------------------------
# List elements can be modified using indexing.

my_list = [1, 2, 3]

my_list[0] = "Simran"
my_list[1] = "shaikh"
my_list[1] = "shaikh"


# -------------------------------------------------------------
# Step 2: Iterate through list using for loop
# -------------------------------------------------------------
# Loop prints each element one by one.

for element in my_list:
    print(element)


# -------------------------------------------------------------
# Step 3: Use range() function
# -------------------------------------------------------------
# range(1, 5) generates numbers from 1 to 4.

# range() this also return the list
for i in range(1, 5):  # 1,2,3,4
    print(i)


# -------------------------------------------------------------
# Step 4: Create new list
# -------------------------------------------------------------
# This list will be used for list operations.

my_list = [1, 2, 3]


# -------------------------------------------------------------
# Step 5: Access elements using indexing
# -------------------------------------------------------------
# Index starts from 0.

print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])


# -------------------------------------------------------------
# Step 6: append() method
# -------------------------------------------------------------
# append() adds element at the end of the list.

my_list.append(4)
print(my_list)

my_list.append(5)
print(my_list)


# -------------------------------------------------------------
# Step 7: extend() method
# -------------------------------------------------------------
# extend() adds multiple elements from another list.

my_list.extend([7, 8, 10, 9])
print(my_list)


# -------------------------------------------------------------
# Step 8: insert() method
# -------------------------------------------------------------
# insert(index, value) adds element at specific position.

my_list.insert(1, "shaikh")
print(my_list)

print(len(my_list))


# -------------------------------------------------------------
# Step 9: Insert value at beginning
# -------------------------------------------------------------
# Adding 0 at index position 0.

my_list.insert(0, 0)
print(my_list)


# -------------------------------------------------------------
# Step 10: Update element using index
# -------------------------------------------------------------
# Replacing element at index 1.

my_list[1] = "javed"
print(my_list)


# -------------------------------------------------------------
# Step 11: remove() method
# -------------------------------------------------------------
# remove() deletes the specified element.

my_list.remove("javed")
print(my_list)


# -------------------------------------------------------------
# Step 12: copy() method
# -------------------------------------------------------------
# copy() creates a duplicate list.

my_copy_list = my_list.copy()

print(my_list)
print(my_copy_list)


# -------------------------------------------------------------
# Step 13: Remove element from copied list
# -------------------------------------------------------------
# Original list remains unchanged.

my_copy_list.remove("shaikh")

print(my_list)
print(my_copy_list)


# -------------------------------------------------------------
# Hindi Explanation:
# - List ke elements ko indexing se update kiya ja sakta hai.
# - for loop list ke har element ko access karta hai.
# - append() end me ek element add karta hai.
# - extend() multiple elements add karta hai.
# - insert() specific position par value insert karta hai.
# - remove() given value ko delete karta hai.
# - copy() list ki duplicate copy banata hai.
# - Copied list me changes karne se original list affect nahi hoti.
#
# English Explanation:
# - List elements can be updated using indexes.
# - for loop iterates through each element.
# - append() adds one element at the end.
# - extend() adds multiple elements.
# - insert() adds element at a specific position.
# - remove() deletes the specified value.
# - copy() creates a duplicate list.
# - Changes in copied list do not affect the original list.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lists are mutable in Python.
# 2. append(), extend(), insert() add elements.
# 3. remove() deletes specific items.
# 4. copy() creates a separate duplicate list.
# 5. for loop and indexing help access list elements.
# -------------------------------------------------------------
```
