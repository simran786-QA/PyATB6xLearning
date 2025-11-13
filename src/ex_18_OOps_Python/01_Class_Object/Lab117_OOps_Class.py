# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Class, Object, Attributes, and Methods
# -------------------------------------------------------------

# Step 1: Define a Class
class Person:
    # Attributes (variables inside the class)
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # -------------------------------------------------------------
    # Step 2: Define Behaviours (methods)

    def talk(self):
        print("I can Talk")

    # Method with Argument and No Return
    def sleep(self, name):
        print("I am a Method!!")
        print("Sleep", name)

    # Method with Argument and Return Value
    def sleep2(self, name):
        print("I am a Method!!")
        return None

    # Method without Arguments and without Return
    def walk(self):
        print("I am walking")

    # Method without Arguments but with Return Value
    def method_walk_return(self):
        return "I am walking"

# -------------------------------------------------------------
# Step 3: Function outside the Class
def function_outside():
    print("Outside function - Not part of class")

# -------------------------------------------------------------
# Step 4: Create Objects (Instances of the Class)
# ObjectRef = ClassName()

geeta = Person()
amit = Person()
navita = Person()

# -------------------------------------------------------------
# Step 5: Access Attributes
print(geeta.name)   # Output: None (default value because not set)

# Hindi:
# Class ke andar humne 'name' attribute banaya hai,
# par abhi usse koi value assign nahi ki gayi, isliye output None hai.
#
# English:
# The 'name' attribute exists, but we haven’t assigned any value yet, so it shows None.

# -------------------------------------------------------------
# Step 6: Call Methods (Behaviours)
geeta.sleep("pramod")

# Hindi:
# Yahan humne object 'geeta' se sleep() method call kiya hai.
# Argument me 'pramod' diya gaya hai.
# Output me method ke print statements display honge.
#
# English:
# Here we called the sleep() method using object 'geeta'.
# The argument 'pramod' is passed, and the method prints its output.

# -------------------------------------------------------------
# Output Example:
# None
# I am a Method!!
# Sleep pramod

# -------------------------------------------------------------
# Step 7: Summary
# 1. Class is a blueprint (template) for creating objects.
# 2. Attributes define data (variables).
# 3. Methods define behaviors (functions inside class).
# 4. 'self' is used to refer to the current object.
# 5. Objects (like geeta, amit) use '.' to access class members.
# -------------------------------------------------------------
