```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python List – Advanced List Methods and Operations
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create a list
# -------------------------------------------------------------
# List containing square numbers.

squares = [1, 4, 9, 16, 25]

print(squares)


# -------------------------------------------------------------
# Step 2: pop() method
# -------------------------------------------------------------
# pop() removes and returns element.
# Default behavior removes last element.

print(squares.pop())
print(squares)

# Removing element from specific index.
print(squares.pop(1))
print(squares)


# -------------------------------------------------------------
# Step 3: clear() method
# -------------------------------------------------------------
# clear() removes all elements from the list.

squares.clear()
print(squares)


# -------------------------------------------------------------
# Step 4: index() and count() methods
# -------------------------------------------------------------
# index() returns first occurrence index.
# count() returns total occurrences.

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))
print(numbers.count(20))


# -------------------------------------------------------------
# Step 5: sort() method
# -------------------------------------------------------------
# sort() arranges list in ascending order.

numbers.sort()
print(numbers)

# Sorting in descending order.
numbers.sort(reverse=True)
print(numbers)


# -------------------------------------------------------------
# Step 6: reverse() method
# -------------------------------------------------------------
# reverse() reverses the list in place.

numbers.reverse()
print(numbers)


# -------------------------------------------------------------
# Step 7: max(), min(), sum()
# -------------------------------------------------------------
# These functions work on numerical lists.

print(max(numbers))   # 40
print(min(numbers))   # 10
print(sum(numbers))   # 120


# -------------------------------------------------------------
# Step 8: List slicing
# -------------------------------------------------------------
# Slicing extracts a portion of the list.

print(numbers)

# Elements from index 1 to 3.
print(numbers[1:4])

# Last element using negative indexing.
print(numbers[-1])


# -------------------------------------------------------------
# Step 9: Membership operators
# -------------------------------------------------------------
# in keyword checks element existence.

print("apple" in numbers)
print(20 in numbers)


# -------------------------------------------------------------
# Step 10: List creation using range()
# -------------------------------------------------------------
# range(1,5) generates numbers from 1 to 4.

l = list(range(1, 5))
print(l)


# -------------------------------------------------------------
# Step 11: Nested Lists
# -------------------------------------------------------------
# List inside another list is called nested list.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing row 1 and column 2.
print(matrix[1][2])


# -------------------------------------------------------------
# Step 12: del statement
# -------------------------------------------------------------
# del removes element by index.

del numbers[0]
print(numbers)


# -------------------------------------------------------------
# Hindi Explanation:
# - pop() element remove karke return karta hai.
# - clear() puri list empty kar deta hai.
# - index() first matching element ka index deta hai.
# - count() element kitni baar repeat hua hai batata hai.
# - sort() ascending order me arrange karta hai.
# - reverse() list ko ulta kar deta hai.
# - max(), min(), sum() numerical operations ke liye use hote hain.
# - Slicing list ka specific part nikalta hai.
# - Nested list me list ke andar list hoti hai.
# - del statement specific element delete karta hai.
#
# English Explanation:
# - pop() removes and returns an element.
# - clear() empties the list.
# - index() gives the first matching index.
# - count() returns frequency of an element.
# - sort() arranges elements in ascending order.
# - reverse() reverses the list order.
# - max(), min(), sum() work on numeric lists.
# - Slicing extracts part of a list.
# - Nested lists contain lists inside lists.
# - del removes elements by index.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lists support many built-in methods.
# 2. pop(), clear(), remove() modify list data.
# 3. sort() and reverse() change list order.
# 4. Slicing and indexing help access elements.
# 5. Nested lists allow multidimensional data storage.
# -------------------------------------------------------------
```
