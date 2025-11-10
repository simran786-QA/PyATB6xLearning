# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Expected vs Actual Output Validation (String Comparison)
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how to compare expected and actual results in automation
# and determine whether a test case passed or failed.

# -------------------------------------------------------------
# 🧪 Scenario:
# In automation, we often validate that the actual output from
# an application or API matches the expected result.
# Example: comparing UI titles, API response messages, etc.

# -------------------------------------------------------------
# ✅ Example Code

expected_title = "Dashboard"
# actual_title = "dashboard "     # Slightly different (case + space)
actual_title = "Dashboard "

# Compare both values (case-insensitive + ignores extra spaces)
if expected_title.strip().lower() == actual_title.strip().lower():
    print("✅ Test Case Passed - Titles match")
else:
    print("❌ Test Case Failed - Titles do not match")

# -------------------------------------------------------------
# 🧠 Explanation (English):
# - `.strip()` removes unwanted spaces.
# - `.lower()` converts text to lowercase for case-insensitive match.
# - If both strings match after cleaning → Test passes.

# -------------------------------------------------------------
# 🧠 Explanation (Hindi):
# - `.strip()` extra spaces हटाता है।
# - `.lower()` uppercase/lowercase को ignore करता है।
# - अगर दोनों strings बराबर हैं → Test Passed, वरना Failed।

# -------------------------------------------------------------
# ✅ Test Data and Output Table (ERT)

# | expected_title | actual_title  | Comparison (after strip/lower) | Output               |
# |----------------|----------------|--------------------------------|----------------------|
# | "Dashboard"    | "Dashboard "   | Equal                          | ✅ Test Passed        |
# | "Dashboard"    | "dashboard "   | Equal                          | ✅ Test Passed        |
# | "Dashboard"    | "Dash Board"   | Not Equal                      | ❌ Test Failed        |
# | "Login"        | "Dashboard"    | Not Equal                      | ❌ Test Failed        |

# -------------------------------------------------------------
# 💡 Real-World QA Use Case:
# Used in automation scripts (like Selenium, Playwright, or API tests)
# to verify UI text, titles, messages, or response values against expected output.
# -------------------------------------------------------------
