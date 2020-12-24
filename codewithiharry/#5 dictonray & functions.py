from time import sleep
# """
dict = {"Kuldeep":"Kohla",
        "Lovish":"Town",
        "Sahil":"Up",
        "Tarun":"tibbi"}

# for i in dict:
#     print(i)

print(dict['Kuldeep'])
# print("\n")
# #user input
# x= input("enter your key to Search:- ").capitalize()
# print(dict[x])

# print("\n")
# key = input("Enter Your Name:- ").capitalize()
# value = input("Enter Your City:- ").capitalize()
# dict.update({key:value})
# x = dict.copy()
# for i in dict:
#     print(i)
#
# print(dict,"\n", x)

# """
"""
dic = {"Kuldeep":"hanumangrah","Sahil":"hmo","Lovish":"hmh"}
for i in dic:
    print(i)

print("\n")
#user = input("Enter Your Name to See profile :- ").capitalize()
updt = input("enter name:- ").capitalize()
updt2 = input("enter city ").capitalize()
dic.update({updt:updt2})
print("\n")
#print(dic[user])
print("\n")

for i in dic:
    print(i)
"""



#to change list into dict use this :-
# ll1 = [["kuldeeo",2],["Lovish",23],["paras",34]]
# xa = dict(ll1)
# print(xa)