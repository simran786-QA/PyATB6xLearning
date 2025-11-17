# -------------------------------------------------------------
# Step 1: Function with One Argument
# -------------------------------------------------------------
# This function prints a greeting message with a given name.

def greet(name):
    print("Hi,", name)


# Calling the function with different values
greet("Pramod")
greet("Amit")
greet(34.56)       # Works because Python allows any data type


# -------------------------------------------------------------
# Step 2: Function with Two Arguments
# -------------------------------------------------------------
# This function prints a full name using first and last name.

def greet_first_last_name(firstname, lastname):
    print("Your full name is,", firstname, lastname)


# Calling the function
greet_first_last_name("Pramod", "Dutta")


# -------------------------------------------------------------
# Step 3: Function without Arguments
# -------------------------------------------------------------
# A simple function that just prints a message.

def FUNCTION_NAME():
    print("Yes")


# Calling the function
FUNCTION_NAME()
