#Faulty Calculator
# Values to be print
# (56+9)=57 (45*3)=555 (56/6)=4

user = int(input("Enter Your 1st Number:- "))

user2 = int(input("Enter Your 2st Number:- "))

print("\n")

list1 = ["+", "-", "*", "/"]
for i in list1:
    print(i)
print("\n")
choice = input("Enter Your Choice from Above").capitalize()

if user == "56" and user2 == "9" or choice == "+":
    print("57")

elif user == "45" and user2 == "3" or choice == "*":
    print("555")

elif user == "56" and user2 == "6" or choice == "/":
    print("4")

elif choice == "+":
    print("Your Answer:- ", user + user2)

elif choice == "-":
    print("Your Answer:- ", user - user2)

elif choice == "*":
    print(user * user2)

elif choice == "/":
    print("your answer", user / user2)

else:
    print("Opps! Wrong Input")
