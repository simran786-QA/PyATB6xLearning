# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Performance Validation – Page Load Time Check
# -------------------------------------------------------------

# 🎯 Objective:
# Validate whether a webpage loads within the acceptable time limit
# (used in performance testing or automation validation).

# -------------------------------------------------------------
# 🧪 Scenario:
# You want to check whether a web page loads within 3 seconds.
# If it exceeds this threshold, mark it as a performance issue.

# -------------------------------------------------------------
# ✅ Example Code

load_time = 4.2  # Measured page load time in seconds

# Define the performance threshold (max acceptable time)
performance_threshold = 3.0

# Compare load time with threshold
if load_time <= performance_threshold:
    print(f"✅ Page loaded successfully in {load_time} seconds")
else:
    print(f"⚠️ Page load too slow: {load_time} seconds")

# -------------------------------------------------------------
# 🧠 Explanation (English):
# - We compare the actual page load time with a threshold.
# - If load_time ≤ threshold → the page passed the performance test.
# - If load_time > threshold → it's too slow.

# -------------------------------------------------------------
# 🧠 Explanation (Hindi):
# - load_time असली लोड टाइम है।
# - अगर load_time ≤ 3 सेकंड → पास (पेज अच्छा लोड हुआ)
# - अगर load_time > 3 सेकंड → फेल (पेज स्लो है)

# -------------------------------------------------------------
# ✅ Example Test Data (ERT)

# | load_time | threshold | Condition         | Output                             |
# |------------|------------|------------------|------------------------------------|
# | 2.5        | 3.0        | 2.5 <= 3.0 (T)  | ✅ Page loaded successfully in 2.5s |
# | 3.0        | 3.0        | 3.0 <= 3.0 (T)  | ✅ Page loaded successfully in 3.0s |
# | 4.2        | 3.0        | 4.2 <= 3.0 (F)  | ⚠️ Page load too slow: 4.2 seconds  |

# -------------------------------------------------------------
# 💡 Real-World QA Use Case:
# - Used in performance testing automation (like Selenium or Lighthouse).
# - Helps measure front-end performance and ensure better user experience.
# -------------------------------------------------------------
