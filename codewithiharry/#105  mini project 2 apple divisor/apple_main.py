"""
harry n(input) number of apples             (apple provided by harry frnds [request few more or less apple])
he want to distribute apples among some children

range as mn to mx and chack n is divisible by it?
print n is diviser or not of range
"""
print(" \t\t\t\tMini Project 2\n*********** By:- Code With Harry ****************\n")
try:
    apples = int(input("Enter how much Apples You got:- "))
    mn = int(input("Enter minimum number:- "))
    mx = int(input("Enter maximum number:- "))+1
except ValueError:
    print("Only Intinger Values are supported")
    exit()


else:
    print('') # for a Blank Line in Output
    for i in range(mn,mx):
        if apples%i == 0:
            print(f'{i} is a Divisor of {apples}')
        elif apples %i!= 0:
            print(f'{i} is not a Divisor of {apples}')
        else:
            print("Something Went Wrong")

