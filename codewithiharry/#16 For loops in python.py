#Name and lolipop

"""
l1 = [["kuldeep",10],["lovish",900],["paras",865],["pytohn",0]]
for item,lolypop in l1:
    print(item,"Has ",lolypop, "lolypops")

print("\n")
print("************************")
print("\n")

for i,n in l1:
    print(i,n)

"""
"""
#to change list into dict use this :-
ll1 = [["kuldeeo",2],["Lovish",23],["paras",34]]
xa = dict(ll1)
print(xa)

print("\n")

#to print this dict in for loop then:-
for items,pops in xa.items():
    print(items,pops)

print("\n")

#for print only items from dict then you can directly do this
for items in xa:
    print(items)
"""

#Harry bhai Questions:-
# from a given list print only number who is greater than 6 and list contains number and variables
list_x = ["Kuldeep",56,34,34,12,45,6,"Lovish"]
for i in list_x:
    if str(i).isnumeric() and i>50:
        print(i)