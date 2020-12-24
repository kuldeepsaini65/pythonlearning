#
# # Oh soldier Prettify my Folder
#
# # path, dictionary file, format
#
# # def soldier("C://", "harry.txt", "jpg")
#
# import os
# def soldier(path, file, format):
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     with open(file) as f:
#         filelist = f.read().split("\n")
#
#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())
#
#         elif os.path.splitext(file)[1] == format:
#             os.rename(file, f"{i}{format}")
#             i +=1
#
#
# path = input(r"Enter your Path:-")
# soldier(path, r"C:\Users\Kuldeep saini/Desktop/files.txt",
#         ".jpg")
#
# print("Done")

import os


def Cleaner(path, txt_file, format):
    os.chdir(path)
    i = 0
    with open(txt_file) as o:
        filelist = o.read().split("\n")

    files = os.listdir(path)
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i = i+1


Cleaner(r"C:/Users/Kuldeep saini/Desktop/helo",
        r"C:/Users/Kuldeep saini/Desktop/Files.txt",
        ".bmp")