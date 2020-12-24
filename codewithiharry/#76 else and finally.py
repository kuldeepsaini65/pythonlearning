
try:
    users_list = {}
    user = input("Enter Your Name:- ").capitalize()
    Pin_Code = int(input("Enter Your Area Pin Code Number:-"))
    users_list.update({user:Pin_Code})
    print(users_list)
except EOFError as eo:
    print(f"EOF error Has Been Occur\nError:-{eo}")
except IOError as io:
    print(f"IO Error Has Been Occur\nError:- {io}")
except Exception as e:
    print(f"****** Excetiopn is running ****** \nError:- {e}")

else:
    print("All Done Sucessfuly")

finally:
    print("This Code Will Run... Whether it catch error or not")
