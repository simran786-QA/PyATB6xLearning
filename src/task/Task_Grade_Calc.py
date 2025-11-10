# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Grade Calculator
# -------------------------------------------------------------
# 🎯 Objective:
# Determine letter grade based on numerical score
# -------------------------------------------------------------
# Grading Scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# -------------------------------------------------------------

score = float(input("Enter your score (0–100): "))

if score < 0 or score > 100:
    print("❌ Invalid score. Please enter between 0 and 100.")
elif score >= 90:
    print("🏆 Grade: A")
elif score >= 80:
    print("🎯 Grade: B")
elif score >= 70:
    print("📘 Grade: C")
elif score >= 60:
    print("⚠️ Grade: D")
else:
    print("❌ Grade: F")

# -------------------------------------------------------------
# 🧠 QA/Automation Relevance:
# - Similar logic is used in test validations and reporting.
# - Conditions mimic pass/fail thresholds in test execution results.
# -------------------------------------------------------------
