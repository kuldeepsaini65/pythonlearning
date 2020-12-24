#5*4*3*2*1

n= int(input("Enter Your Number:- "))
def factorial_itrative(n):
    if n==1:
        return 1
    else:
        return n*factorial_itrative(4)
x = factorial_itrative(n)
print("Value Is - ",x)
