# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Understanding and Using SET in Python
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Creating Sets (Unique Collections)
# -------------------------------------------------------------

# Duplicate values are automatically removed by Python
unique_numbers = {1, 2, 3, 4, 4, 5, 5}
print("Unique Number Set:", unique_numbers)


# -------------------------------------------------------------
# Step 2: Converting List to Set (Removing Duplicates)
# -------------------------------------------------------------

marks_list = [45.2, 33, 33, 45, 21]
marks_set = set(marks_list)
print("List Converted to Set:", marks_set)


# -------------------------------------------------------------
# Step 3: Converting Tuple to Set
# -------------------------------------------------------------

course_tuple = ("TheTestingAcademy", "for", "TheTestingAcademy")
print("Original Tuple:", course_tuple)
print("Tuple Converted to Set:", set(course_tuple))


# -------------------------------------------------------------
# Step 4: Mixed Data Types Inside a Set
# -------------------------------------------------------------

mixed_set = {1, "QA", True, 3.5}
print("Mixed Type Set:", mixed_set)


# -------------------------------------------------------------
# Step 5: Creating an Empty Set
# -------------------------------------------------------------

empty_set = set()
print("Empty Set Type:", type(empty_set))


# -------------------------------------------------------------
# Step 6: Iterating Over a Set
# -------------------------------------------------------------

print("Iterating Through Mixed Set:")
for element in mixed_set:
    print(element)


# -------------------------------------------------------------
# Step 7: Adding & Removing Elements in a Set
# -------------------------------------------------------------

print("Before Adding:", mixed_set)
mixed_set.add(10)
print("After Adding 10:", mixed_set)

mixed_set.remove(10)
print("After Removing 10:", mixed_set)


# -------------------------------------------------------------
# Step 8: Final Example with Boolean Values
# -------------------------------------------------------------

# Note: True behaves like 1, False behaves like 0 inside sets
final_set = {1, "QA", True, False, 3.5}
print("Final Mixed Set:", final_set)
