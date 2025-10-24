# ==============================================================
# Lab019_Grade_Calculator.py
# Author: Simran Shaikh
# Goal: Calculate and display the letter grade for a given score
# ==============================================================

# Grade Scale
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# --------------------------------------------------------------
# Step 1️⃣: Input Handling (with Error Checking)
# --------------------------------------------------------------
try:
    score = float(input("Enter your score (0-100): ").strip())

    # Step 2️⃣: Validate range
    if score < 0 or score > 100:
        print("❌ Invalid score! Please enter a number between 0 and 100.")

    # Step 3️⃣: Apply Grading Logic
    elif score >= 90:
        grade = "A"
        remark = "Excellent work! 🎯"
    elif score >= 80:
        grade = "B"
        remark = "Good job! 👍"
    elif score >= 70:
        grade = "C"
        remark = "Fair performance. Keep improving! 💪"
    elif score >= 60:
        grade = "D"
        remark = "You passed, but study harder next time! 📘"
    else:
        grade = "F"
        remark = "❌ You failed. Don’t give up — try again!"

    # Step 4️⃣: Output result
    if 0 <= score <= 100:
        print(f"\nYour Score: {score}")
        print(f"Your Grade: {grade}")
        print(f"Remark: {remark}")

except ValueError:
    print("⚠️ Invalid input! Please enter a numeric score (e.g., 85 or 72.5).")

# --------------------------------------------------------------
# Step 5️⃣: Summary in Hindi 🇮🇳
# --------------------------------------------------------------
# यूज़र से नंबर (स्कोर) लिया जाता है।
# अगर स्कोर 90 या उससे ज़्यादा है → A ग्रेड
# 80 से 89 → B ग्रेड
# 70 से 79 → C ग्रेड
# 60 से 69 → D ग्रेड
# 0 से 59 → F ग्रेड
# अगर स्कोर गलत है (जैसे -5 या 110), तो वॉर्निंग दिखाता है।
# अगर यूज़र ने नंबर की जगह टेक्स्ट दिया (जैसे “abc”), तो error हैंडल करता है।
# --------------------------------------------------------------

print("\n✅ Program executed successfully by Simran 🌸")
