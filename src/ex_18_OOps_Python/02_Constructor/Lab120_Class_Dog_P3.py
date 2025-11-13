# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Class, Constructor (__init__), and Object References
# -------------------------------------------------------------

# Step 1: Define a Class named Dog
class Dog:
    # ---------------------------------------------------------
    # A. Attributes (Data Members)
    name = None
    breed = None
    height = None
    weight = None

    # ---------------------------------------------------------
    # B. Constructor (Special Method)
    def __init__(self):
        print("I will be called")

    # ---------------------------------------------------------
    # C. Behaviour / Methods
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass  # No action, just a placeholder

# -------------------------------------------------------------
# Step 2: Object Creation (Object References)
chow_ref = Dog()  # Constructor (__init__) will be called automatically
mow_ref = Dog()   # Constructor will run again for this object

# -------------------------------------------------------------
# Step 3: Access Attributes
print(chow_ref.name)  # Output: None
print(mow_ref.name)   # Output: None

# -------------------------------------------------------------
# Step 4: Note
# Dog().talk()  # This line (commented out) would directly create an object and call the 'talk' method.

# -------------------------------------------------------------
# Hindi Explanation:
# 1️⃣ Class Dog me humne 4 attributes (name, breed, height, weight) banaye.
# 2️⃣ Fir ek constructor __init__ banaya — jab bhi hum class ka object banayenge,
#     ye automatic chal jaata hai. Yahan ye "I will be called" print karega.
# 3️⃣ Humne teen methods banaye: bark(), sleep(), aur talk().
#     - bark() → "Barking" print karta hai.
#     - sleep() → "Sleep" print karta hai.
#     - talk() → abhi khali hai (pass likha hai).
# 4️⃣ Jab humne object banaye chow_ref aur mow_ref,
#     tab constructor dono baar run hua (do baar "I will be called" print hoga).
# 5️⃣ Jab humne print(chow_ref.name) likha,
#     to output None aayega, kyunki humne abhi name assign nahi kiya.

# -------------------------------------------------------------
# English Explanation:
# 1️⃣ The Dog class has four attributes — name, breed, height, and weight.
# 2️⃣ The constructor (__init__) runs automatically when an object is created.
#     It prints "I will be called" each time an object i
