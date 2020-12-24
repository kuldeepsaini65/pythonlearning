# raise simply means create own custom output error when user or programme gets some error


# example
# i = input("Enter your Salary:- ")
# if i.isnumeric:
#     raise Exception("Something Went Wrong")
# elif i.isalnum:
#     raise Exception("This Contains AlphaNums")


# Example 2
# user_age = int(input("Enter your Age:- "))
# if user_age == 0:
#     raise ZeroDivisionError("Oops! Age Can't Be 0 ")
# elif user_age < 18:
#     raise Warning("Age lesser")
# elif user_age == 18:
#     raise ValueError(f"{user_age} is Not Valid For Submit")
# elif user_age > 18:
#     print("Age greater")
# print("Continued")


# Example 3
lists = {"Name": ['Kuldeep', 'Lovish', 'Harry'],
         "Class": ['12th Topper', '11th nd 12th Topper', 'Job']}
user_name = input("Enter name:- ").capitalize()
if user_name == "Harry":
    raise ValueError(f"{user_name} Is Blocked By Admin")

elif user_name in lists["Name"]:
    print('Done')

elif user_name not in lists["Name"]:
    print('not listed')
