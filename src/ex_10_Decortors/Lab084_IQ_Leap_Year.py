# -------------------------------------------------------------
# Step 1: Define Function to Check Leap Year
# -------------------------------------------------------------
def check_leap_year(year):
    # Leap year rule:
    # 1️⃣ Year divisible by 4 → possible leap year
    # 2️⃣ But if divisible by 100 → NOT a leap year
    # 3️⃣ Unless divisible by 400 → leap year again
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# -------------------------------------------------------------
# Step 2: Input Year & Call Function
# -------------------------------------------------------------
year = 2025   # Change value to test other years
result = check_leap_year(year)


# -------------------------------------------------------------
# Step 3: Print Result
# -------------------------------------------------------------
print(result)   # True → Leap Year, False → Not Leap Year
