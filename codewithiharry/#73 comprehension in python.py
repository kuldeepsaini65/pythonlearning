# list Comp
ls = [i for i in range(100) if i % 2 == 0]
print(ls)

print("")

# dict comp
dict1 = {i: f"item{i}" for i in range(10)}
print(dict1)

print("")

# set Comp
user_list = [1, 2, 3, 4, 343, 3, 4, 3, 4, 3, 4, 5, 6, 5, 7]
out = {var for var in user_list if var % 2 == 0}
print(out)

print("")

# generator comp
user_list = [1, 2, 3, 4, 343, 3, 4, 3, 4, 3, 4, 5, 6, 5, 7]
out = (i for i in user_list)
print(out.__next__())
print(out.__next__())