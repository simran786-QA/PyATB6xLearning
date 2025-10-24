# ------------------------------------------
# Lab001_Day_Finder.py
# Author: Simran Shaikh
# Topic: match-case Example — Find Day by Number
# ------------------------------------------

# 🔹 Step 1: Take user input
day = int(input("Enter the day number (1-7): ").strip())

# 🔹 Step 2: Use match-case to map number to weekday
match day:
    case 1:
        print("🌞 Monday - Start of the week! Let's get productive.")
    case 2:
        print("🌼 Tuesday - Keep the momentum going!")
    case 3:
        print("🌻 Wednesday - Midweek, you’re halfway there!")
    case 4:
        print("🌷 Thursday - Almost the weekend!")
    case 5:
        print("🌸 Friday - Time to wrap things up!")
    case 6:
        print("🎉 Saturday - Enjoy your weekend!")
    case 7:
        print("🌈 Sunday - Relax and recharge.")
    case _:
        print("❌ Invalid input! Please enter a number between 1 and 7.")

# ------------------------------------------------------------
# 🇮🇳 Hindi Explanation:
# यह प्रोग्राम यूज़र से एक नंबर (1-7) लेता है
# और उसके अनुसार दिन (Monday से Sunday) दिखाता है।
# अगर इनपुट 1 से 7 के बीच नहीं है,
# तो "Invalid input" प्रिंट होता है।
# ------------------------------------------------------------
