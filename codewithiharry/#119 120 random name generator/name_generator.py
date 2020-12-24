from random import randint

"""
loop the number of names 
split the first and last name
join the names 
"""

splitted_names = []
first_name_of_students = []
last_name_of_students = []
names_of_student = []


Name = int(input("How Many Names You Want to Enter ( in Numbers only and Minimum 4 Names) --> "))
for number_of_names in range(Name):
    names = input(f"Please Enter Name {number_of_names+1} --->")
    names_of_student.append(names)

""" First And Last Name Splitter """
for spliting_names in range(len(names_of_student)):
    splitter = names_of_student[spliting_names].split(" ")
    splitted_names.append(splitter)


"""     getting First Name And Last Name  and Storing in an different list  """
for counting in range(len(splitted_names)):
    a = splitted_names[counting]
    last_name = a[1] # getting last name
    last_name_of_students.append(last_name)
    first_name = a[0] # Getting First Name
    first_name_of_students.append(first_name)
    # print(f"{first_name} {last_name}")

""" joining first name and last name """
print("")
length_of_last_name = len(last_name_of_students)


for i in range(len(first_name_of_students)):
    random_last_name = randint(0, length_of_last_name-1)
    print(first_name_of_students[i], last_name_of_students[random_last_name])
# print(splitted_names)
