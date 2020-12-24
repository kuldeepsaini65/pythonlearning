from time import sleep

def choice1():
    l = ["+", "-", "*", "/"]
    for i in l:
        print(i)
        sleep(0.67)

def add():
    """This Is Used For To Find The Sum Of Two Numbers """
    a = int(input("Enter Your First Number:- "))
    b = int(input("Enter Your Second Number:- "))
    add = a+b
    print("Answer:-", add)
    return add


def sub():
    """This IS used to substract Two Digits From each Other"""
    a = int(input("Enter Your First Number:- "))
    b = int(input("Enter Your Second Number:- "))
    sub = a-b
    print("Answer:-", sub)
    return sub

def multply():
    """This Is Used To Multply Two Digits"""
    a = int(input("Enter Your First Number:- "))
    b = int(input("Enter Your Second Number:- "))
    multply = a*b
    print("Answer:-", multply)
    return multply

def div():
    """This Is Used To Divide Two Digits"""
    a = int(input("Enter Your First Number:- "))
    b = int(input("Enter Your Second Number:- "))
    div = a/b
    print("Answer:-", div)
    return div

#to Print Information about Function This Is uesd.
# doc string
#print(add.__doc__)
