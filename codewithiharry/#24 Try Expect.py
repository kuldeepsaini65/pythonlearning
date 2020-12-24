

print("Hello Welocome To My Code:-------")
# To Handle Error this is for to not stop program due to error.
# error will not effect our program. and it will continuous run at last

try:
    name1 = int(input("Please Enter Your Name:- "))
    print(name1)

except:
    print("Ops! You Not Typed Your Name Properly..\nPlease enter your name without number and symboles : )")

# print error without Stop program
try:
    inp = int(input("Enter Your Mobile Number:- "))
    print(inp)
except Exception as e: # this will store error in e and then error will be printed
    print(e)