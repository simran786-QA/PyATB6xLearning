# -----------------------------------------------
# Lab020_TestType_Selector.py
# Author: Simran Shaikh
# Topic: Decision Making in Python (if-elif-else & match-case)
# -----------------------------------------------

# ------------------------------------------------
# Objective:
# A QA Engineer needs to choose which type of test to run.
# The program will take the test type as input and display the action.
# ------------------------------------------------

# ------------------------------------------------
# 🪄 Step 1: Take user input
# ------------------------------------------------
print("🔹 Enter which Test you want to run")
test_type = input("Enter the Test Type (API, UI, Performance, Security): ").strip().lower()

# ------------------------------------------------
# Step 2: Using if-elif-else (Traditional Method)
# ------------------------------------------------
print("\n📘 Using if-elif-else Method:")
if test_type == "api":
    print("👉 Running POSTMAN API Testcases.")
elif test_type == "ui":
    print("👉 Running Selenium UI Testcases.")
elif test_type == "performance":
    print("👉 Running Performance Testcases with JMeter.")
elif test_type == "security":
    print("👉 Running Security Testcases using OWASP ZAP.")
else:
    print("❌ Invalid Test Type! Please enter a valid one (API/UI/Performance/Security).")

# ------------------------------------------------
#  Step 3: Using match-case (Modern Python 3.10+)
# ------------------------------------------------
print("\n📗 Using match-case Method:")
match test_type:
    case "api":
        print("🚀 Running POSTMAN API Testcases.")
    case "ui":
        print("🚀 Running Selenium UI Testcases.")
    case "performance":
        print("🚀 Running Performance Testcases with JMeter.")
    case "security":
        print("🚀 Running Security Testcases using OWASP ZAP.")
    case _:
        print("⚠️ Invalid Test Type! Please check your input.")

# ------------------------------------------------
# 💡 Step 4: Additional Concepts
# ------------------------------------------------
# 🧩 .strip()   -> Removes leading and trailing spaces
# 🧩 .lower()   -> Converts the input to lowercase for case-insensitive comparison
# 🧩 case _     -> Acts like a default 'else' condition in match-case
# ------------------------------------------------

# 🇮🇳 HINDI EXPLANATION ---------------------------------------------
# यह प्रोग्राम यूज़र से पूछता है कि वह कौन सा टेस्ट रन करना चाहता है (API, UI, Performance, Security)।
# फिर यह दो तरीकों से निर्णय लेता है:
# 1️⃣ if-elif-else -> पुराना तरीका, हर कंडीशन को मैन्युअली चेक करता है।
# 2️⃣ match-case -> नया तरीका (Python 3.10+), जिससे कोड क्लीन और आसान बनता है।
# ------------------------------------------------
