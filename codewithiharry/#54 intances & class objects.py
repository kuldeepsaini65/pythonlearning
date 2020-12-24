# instance means object(kuldeep.name) has its own property

class employee:
    no_of_chances = 10
    pass


rohan = employee()
rohan.name = "Rohan sing "
# print(employee.__dict__) this will return Dictonary
# print(name.__dict__)
print(employee.no_of_chances)
print(rohan.name)
# We cant change no_of_Chances for a specific person to change this only one Method:-
# employee.no_of_chances = 5

# if we change no_of_leaves by this method :-
# rohan.no_of_chances = 45
# then it will create new stored data that is intences but it not change orrignal one
