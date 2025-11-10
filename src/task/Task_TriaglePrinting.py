# Input number of rows
n = 3

# Outer loop for rows
for i in range(1, n + 1):
    # Inner loop for printing stars
    for j in range(i):
        print("*", end=" ")
    print()  # Move to next line after each row
