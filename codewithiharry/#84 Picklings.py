import pickle

""" Pickling With pickle.dump() """
# string = "Kuldeep Is Unlucky boy and there os no Love for him "
# file = "Library.txt"
# a = open(file, "wb")
# pickle.dump(string, a)

""" Pickling With pickle.dumps()"""
# string = "Hello my frind how are you. i am sure that you are fine"
# with open("datafile.pkl", "wb") as w:
#    w.write(pickle.dumps(string))


""" pickling a dictionary """

# string = {"students_names": [{
#     "kuldeep saini": "BCA 1st Year",
#     "Lovish Kiroriwal": "BA 1st year"
# }]}
# file = "Library.txt"
# opn = open(file, "wb")
# opn.write(pickle.dumps(string))


""" Extracting a Data from a Text File And Converting it into Binary and Sending Into Another File """
# s = open("Contest.txt", "r")
# r = s.read()
# file = "Library.txt"
# f = open(file, "wb")
# pickle.dump(r, f)

""" Unpickling a data """
# with open("testing.pkl",'rb') as t:
#     oy = pickle.load(t)
#     print(oy)
