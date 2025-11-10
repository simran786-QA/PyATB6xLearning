# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Retry Logic for API Response Validation
# -------------------------------------------------------------

# 🎯 Objective:
# Simulate an API retry mechanism using a while loop.
# The test retries up to 3 times until it gets a successful response (status code 200).

# -------------------------------------------------------------
# 🧪 Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed
# -------------------------------------------------------------

# Initialize counters and variables
attempt = 1
max_attempt = 3
response = None

# Start retry mechanism
while attempt <= max_attempt:
    print(f"Attempt {attempt}: ", end="")
    response = int(input("Enter the Response Code ➜ "))

    if response == 200:
        print("✅ Test Passed (Success on Attempt", attempt, ")")
        break
    else:
        print("❌ Failed Attempt", attempt)
        attempt += 1  # Increment attempt count

# Final check after loop completion
if response != 200:
    print("🚨 Test Failed after 3 attempts. Please check network or API stability.")

# -------------------------------------------------------------
# 🧠 Explanation:
# - Uses a while loop to retry an API call up to 3 times.
# - If status code becomes 200, loop stops immediately using 'break'.
# - If all retries fail, prints failure message.
# -------------------------------------------------------------

# ✅ Example Test Data (ERT)
# | Attempt | Input Response | Output                   |
# |----------|----------------|--------------------------|
# | 1        | 500            | ❌ Failed Attempt 1       |
# | 2        | 200            | ✅ Test Passed            |
# | 3        | (not reached)  | -                        |
# | 1–3      | all ≠ 200      | 🚨 Test Failed after 3 attempts |

# -------------------------------------------------------------
# 💡 QA Use Case:
# - Common in automation frameworks (API + UI)
# - Retry flaky API calls due to network or latency issues
# - Helps in building resilient test suites
# -------------------------------------------------------------
