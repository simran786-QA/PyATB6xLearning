# -------------------------------------------------------------
# Step 1: List of Numbers
# -------------------------------------------------------------
# We want to apply square operation on each number in this list.

numbers = [1, 2, 3, 4, 5]


# -------------------------------------------------------------
# Step 2: Function to square a number
# -------------------------------------------------------------
# Returns the square of x.
# (Hindi: Yeh function number ka square return karta hai.)

def square(x):
    return x ** 2


# -------------------------------------------------------------
# Step 3: Apply map() to square all numbers
# -------------------------------------------------------------
# map() applies the square() function to every item in the list.

squared_numbers = list(map(square, numbers))


# -------------------------------------------------------------
# Step 4: Print the squared numbers
# -------------------------------------------------------------
# Expected Output: [1, 4, 9, 16, 25]

print(squared_numbers)
