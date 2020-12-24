# # * pattern
# num = int(input('How Much Rows Do You Want To Print:- '))
# print("Notice:- Type 1 for positive \n \t\t Type 0 For Reverse\n ")
# row = input("Enter Here:- ")
# new = bool(row)
#
# if new==1:
#     for i in range(1, num+1):
#         for j in range(1,i+1):
#             print("*", end=" ")
#         print()
# elif new ==0 :
#     for i in range(num,0,-1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()

one = int(input("Enter Here For Rows:- "))
print("Enter 0 or 1")
two = int(input())
new = bool(two)
if new ==True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
print("Program Finish")
