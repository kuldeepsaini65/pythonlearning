from functions import *
from time import sleep

while(True):
        usr = input("Enter Your Username:- ")
        pswd = input("Enter Your Passward:- ")
        if usr=="admin" and pswd=="admin123":
            print("Welcome User-")
            break
        else:
            print("Passward Or Username is Incorrect!\n Try Again\n")
            continue


while(True):
    print("\n")
    choice1()
    sleep(0.50)
    choice = input("\nEnter Symbole as given Above:-")
    sleep(1)
    print("\n")
    if choice == "+":
        add()
        sleep(1)
    elif choice == "-":
        sub()
        sleep(1)
    elif choice == "*":
        multply()
        sleep(1)
    elif choice == "/":
        div()
        sleep(1)
    else:
        print("You Typed Incorrect Keyword Please Choose options From Above;-")
        sleep(1)
        continue