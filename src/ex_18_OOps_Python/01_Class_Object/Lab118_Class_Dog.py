# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Class, Object, Attributes & Method Example
# -------------------------------------------------------------

# Step 1: Create a Class named 'Dog'
class Dog:
    # -------------------------------------------------------------
    # A. Attributes (Data Members)
    name = None
    breed = None
    height = None
    weight = None

    # -------------------------------------------------------------
    # B. Methods (Behaviours)

    # Method 1: bark()
    def bark(self):
        print("Barking")
        # print(name)  # This will give an error because 'name' must be accessed via self
        print(self.name)  # Correct way — accessing object's own 'name'

    # Method 2: talk()
    def talk(self):
        print("Talking")

# -------------------------------------------------------------
# Step 2: Code outside the class
print("Outside ?")   # This line just prints a message before creating any object.

# -------------------------------------------------------------
# Step 3: Create Objects (Instances) of the Class
chow = Dog()      # Object 1 created
# Dog() — Creates a new object in memory
# chow — Reference variable that points to that Dog object

rancho = Dog()    # Object 2 created

# -------------------------------------------------------------
# Step 4: Assign attribute values to each object
chow.name = "ChowChow"
chow.breed = "Bulldog"
chow.height = "2.5ft"
chow.weight = "25kg"

rancho.name = "Rancho"
rancho.breed = "Labrador"
rancho.height = "3ft"
rancho.weight = "30kg"

# -------------------------------------------------------------
# Step 5: Call Methods
chow.bark()     # Output: Barking + ChowChow
rancho.bark()   # Output: Barking + Rancho

# -------------------------------------------------------------
# Step 6: Summary (Explanation)
# Hindi:
# - Humne ek class banayi Dog.
# - Uske andar kuch attributes (name, breed, height, weight) define kiye.
# - Kuch methods (bark, talk) likhe jo dog ke actions dikhate hain.
# - 'self' har method ka pehla argument hota hai jo current object ko refer karta hai.
# - Fir humne 2 objects banaye: chow aur rancho, unke liye alag-alag data set kiya.
# - Fir unhone apna-apna bark() method call kiya.

# English:
# - We defined a class 'Dog' with attributes and methods.
# - 'self' refers to the current object that is calling the method.
# - We created two objects: chow and rancho.
# - Each object has its own separate data (name, breed, etc.).
# - When we call bark(), Python automatically passes that object as 'self'.
# -------------------------------------------------------------
