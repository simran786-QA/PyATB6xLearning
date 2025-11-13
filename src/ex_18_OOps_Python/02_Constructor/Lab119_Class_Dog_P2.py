# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Class, Object, Constructor (__init__), and Method
# -------------------------------------------------------------

# Step 1: Code before class definition
print("Outside the class")

# -------------------------------------------------------------
# Step 2: Define a class named MobilePhone
class MobilePhone:
    # Attribute (Data Member)
    model = None

    # ---------------------------------------------------------
    # Constructor Method (Special Method)
    def __init__(self):
        print("DC")  # This will run automatically when an object is created.

    # ---------------------------------------------------------
    # Regular Method
    def talk(self):
        print("Hi, talking")

# -------------------------------------------------------------
# Step 3: Create Object of the Class
iphone = MobilePhone()
# Explanation:
# - When we create an object like 'iphone = MobilePhone()', Python automatically
#   calls the constructor `__init__()` inside the class.
# - So the output will include "DC" printed from inside the constructor.

# -------------------------------------------------------------
# Step 4: Call the talk() Method
iphone.talk()
# This manually calls the 'talk' function of that object.
# Output → "Hi, talking"

# -------------------------------------------------------------
# Step 5: Print message outside the class again
print("Outside the class2")

# -------------------------------------------------------------
# Hindi Explanation:
# 1️⃣ Pehle humne ek print statement likha "Outside the class" — class ke bahar.
# 2️⃣ Fir humne ek class banayi MobilePhone.
#     - Usme ek attribute hai: model
#     - Ek constructor method hai: __init__()
#       → Ye automatic chal jata hai jab object banate hain.
#     - Ek normal method hai: talk(), jo manually call karna padta hai.
# 3️⃣ Jab humne object banaya (iphone = MobilePhone()), tab constructor chala aur “DC” print hua.
# 4️⃣ Fir humne talk() method call kiya — "Hi, talking" print hua.
# 5️⃣ Fir last line "Outside the class2" print hui.

# -------------------------------------------------------------
# English Explanation:
# 1️⃣ First, we print a message "Outside the class" (outside any class).
# 2️⃣ Then we define the class MobilePhone with:
#     - One attribute: model
#     - One constructor: __init__(), which runs automatically on object creation.
#     - One method: talk(), which needs to be called manually.
# 3️⃣ When we create the object 'iphone', the constructor prints "DC".
# 4️⃣ Then calling 'iphone.talk()' prints "Hi, talking".
# 5️⃣ Finally, we print another message outside the class — "Outside the class2".
# -------------------------------------------------------------
