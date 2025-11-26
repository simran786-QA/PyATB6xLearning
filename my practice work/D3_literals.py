# Numeric Literals
a = 10
b = 3.14
c = 2 + 3j

# String Literal
name = "Simran"

# Boolean Literals
is_active = True

# None Literal
data = None

# Collection Literals
numbers = [1, 2, 3]
info = {"city": "Mumbai"}

print(a, b, c)
print(name)
print(is_active)
print(data)
print(numbers)
print(info)


#litral used in automation
BASE_URL = "https://api.server.com"     # string literal
TIMEOUT = 30                            # numeric literal
IS_DEBUG = False                        # boolean literal

headers = {"Content-Type": "application/json"}   # dict literal


#API या DB से NULL आए तो Python उसे handle करता है:
response_value = None
if response_value is None:
     print("no data returned")

