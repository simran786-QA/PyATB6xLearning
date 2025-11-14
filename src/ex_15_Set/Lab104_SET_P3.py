# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Working with Sets, Looping, and Adding Elements in Python
# -------------------------------------------------------------


# -------------------------------------------------------------
# Step 1: Create a Set
# -------------------------------------------------------------
# Hindi:
# Yaha hum ek list ko set me convert kar rahe hain.
# Set automatically duplicate values ko remove kar deta hai.
#
# English:
# Here we convert a list into a set.
# Sets automatically remove duplicate elements.

set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print("Initial Set:", set1)

# Length of the set
print("Length of Set:", len(set1))


# -------------------------------------------------------------
# Step 2: Loop Through the Set
# -------------------------------------------------------------
# Hindi:
# Set ke har element ko loop ke through print kar rahe hain.
#
# English:
# Printing each element of the set using a loop.

for item in set1:
    print("Element:", item)


# -------------------------------------------------------------
# Step 3: Adding Elements to Set
# -------------------------------------------------------------
# Hindi:
# Add() function se hum set me naya element add kar sakte hain.
# Agar element pehle se exist karta ho, to dubara add nahi hota.
#
# English:
# Using add() to insert an element into the set.
# If the value already exists, it will not be added again.

set1.add("Pramod")
set1.add("Pramod")   # Duplicate, will not be added again

print("Set After Adding Elements:", set1)
