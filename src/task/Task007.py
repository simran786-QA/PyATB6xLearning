# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Authentication Logic – Login Validation
# -------------------------------------------------------------

# 🎯 Objective:
# Validate user login credentials (username and password)
# before granting access. Used in login/authentication testing.

# -------------------------------------------------------------
# 🧪 Scenario:
# Check if the user can log in with the correct username and password.
#
# I/P:
#   username = "admin"
#   password = "1234"
#
# O/P:
#   ✅ Login Successful
#
# For any incorrect credentials:
#   ❌ Invalid Credentials

# -------------------------------------------------------------
# ✅ Example Code

# Take input from the user
username = input("Enter Username: ")
password = input("Enter Password: ")

# Validate username and password
if username == "admin" and password == "1234":
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")

# -------------------------------------------------------------
# 🧠 Explanation (English):
# - Both username and password must match expected values.
# - If either one fails, login is rejected.

# -------------------------------------------------------------
# 🧠 Explanation (Hindi):
# - Username और Password दोनों सही होने चाहिए।
# - अगर कोई भी गलत है → ❌ Invalid Credentials प्रिंट होगा।

# -------------------------------------------------------------
# ✅ Example Test Data (ERT)

# | username | password | Condition                           | Output                  |
# |-----------|-----------|------------------------------------|--------------------------|
# | admin     | 1234      | True and True → True               | ✅ Login Successful       |
# | admin     | 4321      | True and False → False             | ❌ Invalid Credentials    |
# | user      | 1234      | False and True → False             | ❌ Invalid Credentials    |
# | user      | 4321      | False and False → False            | ❌ Invalid Credentials    |

# -------------------------------------------------------------
# 💡 Real-World QA Use Case:
# - Common in UI automation (Selenium, Playwright)
# - Also used in API testing (login endpoint validation)
# - Helps verify authentication flow and security logic
# -------------------------------------------------------------
