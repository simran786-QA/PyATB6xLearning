# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Set Comprehension and Frozen Set in Python
# -------------------------------------------------------------


# -------------------------------------------------------------
# Step 1: Set Comprehension
# -------------------------------------------------------------
# Hindi:
# Yaha hum set comprehension use kar rahe hain, jo ek short-cut
# tareeka hai set banane ka. Yeh har x ka square set me store karega.
#
# English:
# Here we use set comprehension, which is a compact way
# to create sets. It stores square of each number in the set.

squares = {x ** 2 for x in range(5)}
print("Squares Set:", squares)


# -------------------------------------------------------------
# Step 2: Frozen Set (Immutable Set)
# -------------------------------------------------------------
# Hindi:
# Frozenset ek immutable set hota hai. Matlab:
# Ek baar ban gaya, to aap usme add, remove ya update nahi kar sakte.
#
# English:
# A frozenset is an immutable version of a set.
# Once created, you cannot add, remove, or modify elements.

my_list = [1, 2, 3, 3]   # Duplicate values will be removed
fset = frozenset(my_list)
print("Frozen Set:", fset)

# fset.add(4)  # This will give an error: frozenset does not support add()

# -------------------------------------------------------------
# Summary:
# 1. Set Comprehension → Creates sets in a single line.
# 2. Frozenset → Immutable set (cannot be changed).
# -------------------------------------------------------------
