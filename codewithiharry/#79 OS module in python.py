import os
# # to Get The Current Working Directory
# print(os.getcwd())
#
# # to Change The Directory
# os.chdir("C:/Users/Kuldeep saini/Downloads")
# # print(os.getcwd())
#
# x = dir(os)
# for i in x:
#     print(i)
import stat

paths = "C:/Users/Kuldeep Saini/Desktop"

# os.mkdir("Testing")

# os.rename("Testing", "KUldeep")

# os.chdir(paths)
# listing = os.listdir()
# for x in listing:
#     print(x)

""" Deleting The File   """
file = "YouTube.txt"
path = os.path.join(paths, file)
os.remove(path)

# print(os.environ.get("Path"))
# print(os.path.join(paths, "Tor Browser"))