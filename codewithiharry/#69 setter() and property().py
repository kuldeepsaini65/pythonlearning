class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname + self.lname}@gmail.com"

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email Is Not Given"
        return f"{self.fname}.{ self.lname}@trickindia.xyz"

    @email.setter # now here if user changed name or email then it will automatically change user email or name
    def email(self, string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None




kuldeepsaini = employee("Kuldeep", "Saini")
kuldeepsaini.email = "rohan.das@gmail.com"
# print(kuldeepsaini.email)
# del kuldeepsaini.email
# print(kuldeepsaini.email)
# print(employee.details())
# print(kuldeepsaini.fname)
# print(kuldeepsaini.email)
# kuldeepsaini.fname = "aditya"
# print(kuldeepsaini.email)
# del kuldeepsaini.email
# kuldeepsaini.fname = "adity"
# print(kuldeepsaini.email)