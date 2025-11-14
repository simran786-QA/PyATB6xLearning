# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Set Operations in Python (Union, Intersection, Difference)
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: UNION Operation
# -------------------------------------------------------------
# Hindi:
# Do sets ko jodne ke liye union use hota hai. Duplicate values remove ho jati hain.
#
# English:
# Union combines elements of both sets and removes duplicates.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

union_result = set1.union(set2)
print("Union Result:", union_result)


# -------------------------------------------------------------
# Step 2: INTERSECTION Operation
# -------------------------------------------------------------
# Hindi:
# Intersection sirf un elements ko return karta hai jo dono sets me common hote hain.
#
# English:
# Intersection returns only the common elements between two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection_result = set1.intersection(set2)
print("Intersection Result:", intersection_result)


# -------------------------------------------------------------
# Step 3: DIFFERENCE Operation (set1 - set2)
# -------------------------------------------------------------
# Hindi:
# Difference operation aise elements return karta hai jo set1 me hon,
# but set2 me NA ho.
#
# English:
# Difference returns elements present in set1 but NOT present in set2.

difference_1 = set1.difference(set2)
print("Difference (set1 - set2):", difference_1)


# -------------------------------------------------------------
# Step 4: DIFFERENCE Operation (set2 - set1)
# -------------------------------------------------------------
# Hindi:
# Ab hum reverse difference kar rahe hain (set2 - set1).
#
# English:
# Reverse difference gives elements from set2 that are NOT in set1.

difference_2 = set2.difference(set1)
print("Difference (set2 - set1):", difference_2)
