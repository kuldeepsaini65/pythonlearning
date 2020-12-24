from time import sleep

#1
#checking Result For class !2th
name1 = ["Kuldeep","Lovish","Paras","Harman","Rahul"]
user_result = input("Enter Your First Name:- ").capitalize()
if (user_result in name1):
    print("Congratulations! ")

else:
    print("Oops! Get Lost You fool")
#We can also use "not in "function as done upper


#2
#Harry Yt Question:-
# Driving Licence Apploication "age Identifier"
print("Driving Lisence Code:- \n")
print("*******************************")
user = int(input("Enter Your Age :-"))
if user>18:
    print("Congrlatutions! Your Selected For Licence ")

elif user==18:
    print("Sorry! We cant't Decide Now. Please Phisicaly Persent In our Office For Appliying")

else:
    print("Sorry Your Age is ",user)

print("********************************")

sleep(5)