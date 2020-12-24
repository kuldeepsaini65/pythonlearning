import json

# data = {
#     "emp_detail": [
#         {
#             "emp_name": "shubham",
#             "email": "shubham@gmail.com",
#             "job_profile": "iteral",
#         },
#         {
#             "emp_name": "nikhil",
#             "email": "nikhil@gmail.com",
#             "job_profile": "developer"
#         },
#         {
#             "emp_name": "gaaurav",
#             "email": "gaurav@gmail.com",
#             "job_profile": "Full time"
#         }
#     ]
# }
# x = json.dumps(data,indent=3)
# print(x)

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

#convert into JSON:
# y = json.dumps(x)

#Convert into JSON (But easily to Read)
# y = json.dumps(x, indent=4)

#sepearator
# y = json.dumps(x, indent=1, separators=(".", "+"))

#the result is a JSON string:
# print(y)

print("\n\nHello\n\n")
# ******   json.load()    ******
# Python program to read decode only json file


# Opening JSON file
f = open('files1.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_detail']:
    print(i)

# Closing file
f.close()
