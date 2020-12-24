import random
from time import sleep

# a = random.randint(0,10)
# print(a)
print()
print("Please Check Your Name. If Registered Then Please Wait For Results if Now than Register From Below")
print()
with open("Contest.txt", "rt") as cont:
    for i in cont:
        print(i, end="")

print()
print("------To Participate In Our Contest Please Submit Your Name-----")
print("To Quit Type - Q")
while True:
    names = input("Enter Your Name Here:- ").capitalize()
    print()
    if names == "Q":
        print("Exited ")
        break
    winer_name = names
    with open("Contest.txt", "a") as wrt:
        wrt.write((winer_name+"\n"))
    for j in winer_name:
        print(j, end="")

    sleep(2)
    print(" Your Registration Done Successfully ")
    print()
    print("To See The List Of Candidate Then Press:- List")
    inp_list = input("List/Quit").capitalize()
    if inp_list == "List":
        with open("Contest.txt") as list1:
            for viewer in list1:
                print(viewer, end="")
    elif inp_list == "Quit":
        break

while True:
    with open("Contest.txt") as final:
        final_call = list(final)
    x = random.choice(final_call)
    print(x)
    print()
    again = input("Type 1 to re-start Random Winner Program \nType 0 for Exit:- ").capitalize()
    if again == "1":
        continue
    elif again == "Q":
        break
