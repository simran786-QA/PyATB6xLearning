# Dictionary ek data structure hai jisme data "key-value" pairs ke form me store hota hai.
# Example: {"name": "Aman", "age": 34}
# Dictionary ka use hum testing data, API response, ya user details store karne ke liye karte hain.

# Step 1: Create a dictionary
my_dict = {
    "name": "Aman",        # Key = "name", Value = "Aman"
    "age": 34,             # Key = "age", Value = 34
    "role": "SDET",        # Key = "role", Value = "SDET"
    "exp": 3               # Key = "exp", Value = 3 years
}

# Step 2: Print the complete dictionary
print(my_dict)
# Output: {'name': 'Aman', 'age': 34, 'role': 'SDET', 'exp': 3}

# Step 3: Access specific values using keys
print(my_dict["age"])   # Prints 34
print(my_dict["role"])  # Prints 'SDET'

# Step 4: Update a value
# Suppose Aman ka role change ho gaya hai, ab wo Manual Tester hai
my_dict["role"] = "Manual Tester"
print(my_dict)
# Output: {'name': 'Aman', 'age': 34, 'role': 'Manual Tester', 'exp': 3}

# Step 5: Delete a key-value pair from dictionary
# Hum 'age' ko dictionary se hata rahe hain
del my_dict["age"]
print(my_dict)
# Output: {'name': 'Aman', 'role': 'Manual Tester', 'exp': 3}

# Step 6: Iterate (loop) through all key-value pairs
# .items() ek method hai jo dictionary ke saare key aur unke values return karta hai as tuples
for key, value in my_dict.items():
    print(key, "->", value)
# Output:
# name -> Aman
# role -> Manual Tester
# exp -> 3

# Step 7: Check if a key exists in dictionary or not
print("age" in my_dict)   # False, kyunki age delete kar diya
print("role" in my_dict)  # True, kyunki role abhi bhi dictionary me hai

"""test_case = {
    "id": "TC_001",
    "name": "Login Functionality",
    "expected_result": "User should login successfully",
    "status": "Passed"
}

for key, value in test_case.items():
    print(f"{key} -> {value}")
"""
"""Output: id -> TC_001

name -> Login Functionality
expected_result -> User should login successfully
status -> Passed
"""



