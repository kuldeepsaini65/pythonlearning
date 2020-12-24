#harry Bhai Question Guess the Hint Number


#Gussed Number=26
#Guss Limit = 6
num = 26
limit = 6
while(True):
    print("\nHint:- Number 20-35 k Bhich Mai Hai")
    inp = int(input("Enter Your Number To Be Guess:- "))
    limit = limit-1
    print(limit,"****Chances Left****")
    if limit==0:
        print("Limit Reached\n-----Game Over-------")
        break
    elif inp==num:
        print("Bhai Kadak! Ek dum Correct Answer\n")
        break
    elif inp<num:
        print("Bhai Thoda Sa Jayda Kro Number\n")
    else:
        print("Bhai Apka Number Bhout Jayada ho Gaya Thoda Km Kre \n")
