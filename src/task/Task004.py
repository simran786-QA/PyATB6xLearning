# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: If-Else – API Response Validation
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how to use if-else statements to validate an API response code.

# -------------------------------------------------------------
# 🧪 Scenario:
# You receive an API response code from your test script.
# You need to check whether the API call was successful (status 200)
# or failed (any other status).

# -------------------------------------------------------------
# ✅ Example Code

# Input: API response code (simulate via user input)
response = int(input("Enter API Response Code: "))

# Condition check
if response == 200:
    print("✅ Passed API Request")
else:
    print("❌ Failed API Request")

# -------------------------------------------------------------
# 🧠 Explanation (English):
# - If the API response code equals 200, that means success.
# - Any other code (like 400, 401, 404, 500) means failure.

# -------------------------------------------------------------
# 🧠 Explanation (Hindi):
# - अगर response code 200 है तो API call successful मानी जाएगी।
# - अगर कोई और code है (जैसे 404 या 500), तो वो Failed मानी जाएगी।

# -------------------------------------------------------------
# ✅ Test Data and Output Table (ERT)

# | Input (response) | Condition (response == 200) | Output                 |
# |------------------|-----------------------------|------------------------|
# | 200              | True                        | ✅ Passed API Request   |
# | 404              | False                       | ❌ Failed API Request   |
# | 500              | False                       | ❌ Failed API Request   |
# | 201              | False                       | ❌ Failed API Request   |

# -------------------------------------------------------------
# 💡 Real-World QA Use Case:
# In API testing (Postman, Python `requests`, or automation tools),
# response status codes help validate whether an endpoint works correctly.
# You can use this logic inside automated test scripts to mark a test pass/fail.
# -------------------------------------------------------------
