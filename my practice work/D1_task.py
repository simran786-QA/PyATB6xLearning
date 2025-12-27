#Take a input from a user and print the table
num = int(input("enter your number: "))
for i in range(1,11):
    print(num,"x",i,"=",num * i)


    """Hinglish Explanation (Easy)

input() → user se value leta hai (string hoti hai)
int() → string ko number me convert karta hai
for i in range(1, 11) → loop 1 se 10 tak chalega
number * i → table ka multiplication logic"""