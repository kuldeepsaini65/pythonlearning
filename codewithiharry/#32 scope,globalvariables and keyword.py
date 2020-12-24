# x = 10 #Global Value
#
# def var1():
#     # x = 1 # local Value
#     global x
#     x = x+200
#     print(x)
# var1()

def harry():
    x= 20
    def rohan():
        global x
        x = 800 #it will search for x in global if not found then it will create new
    print("Before Calling Rohan",x)
    rohan()
    print("After Calling Rohan",x)

harry()
print(x)

