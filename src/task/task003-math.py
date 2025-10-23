# Program: Calculate the Area of a Circle
# Author: Simran Shaikh
#  Goal: Use formula area = π × r² (Take π as 3.14 or math.pi)

import math

# Step 1️⃣: Take input from user (radius of the circle)
radius = float(input("Enter the radius of the circle in meters: "))

# Step 2️⃣: Apply the formula for area of circle
# Formula: area = π × r²
area = math.pi * pow(radius, 2)

# Step 3️⃣: Display raw and formatted output
print("\n--- Circle Area Calculation Result ---")
print(f"Given Radius: {radius} meters")
print(f"Area of the circle is: {area} square meters")
print(f"Area (rounded to 2 decimal places): {area:.2f} sq.m")

# Step 4️⃣: Fun Example Message
print(f"\nHi Simran! 😊 A circle with radius {radius}m has an area of approximately {area:.2f} square meters.")
