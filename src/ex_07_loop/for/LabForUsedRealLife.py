# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop – Running Multiple Test Cases
# -------------------------------------------------------------

# 🎯 Objective:
# Automate repetitive actions like running multiple test cases using a loop.

# -------------------------------------------------------------
# ✅ Concept:
# range(start, stop) generates a sequence of numbers from start → stop-1.
# For example, range(1, 6) → 1, 2, 3, 4, 5 (5 test cases)

# -------------------------------------------------------------
# ✅ Example: Run 5 test cases one by one
for test_id in range(1, 6):
    # You can print in two ways:
    # 1️⃣ Using f-string formatting (modern & clean)
    # print(f"Running the test case: {test_id}")

    # 2️⃣ Using normal print with commas (older but valid)
    print("Running the test case:", test_id)

# -------------------------------------------------------------
# 🧩 Output:
# Running the test case: 1
# Running the test case: 2
# Running the test case: 3
# Running the test case: 4
# Running the test case: 5

# -------------------------------------------------------------
# 🧠 Real-world Analogy:
# Like executing 5 automated scripts in sequence (API/UI tests)
# Each iteration = one test case execution.
