from time import timezone
"""
i = 0
while(True):
    if i + 1 < 5:
        i = i + 1
        continue
    print("hello ", end=" ")
    if (i==44):
        break
    i = i+  1
"""

"""
#harry bhai question
# take input from user and take again and again yet the user not enter 100
while(True):
    inp = int(input("Enter Your Number:- "))
    if inp>=100:
        print("Congrlats!")
        break
    else:
        print("Try Again \n")
        continue
"""

#Aunthontcation Codeing
while(True):
    username = input("\nEnter Your Username:-").lower()
    passwd = input("Enter Your Passward:- ").lower()
    if username == "admin" and passwd == "admin123":
        print("\nCongrlatutions! ")
        break
    else:
        print("\nIncorrect Username Or Passward \nTry Again!\n")
        continue

print("Welcome Admin Sir!")
