class students:
    no_of_leaves = 400

    def __init__(self, name, std, rollno):  # Constructor
        self.name = name
        self.std = std
        self.roll_no = rollno

    def details(self):
        print(f"Name = {self.name} \nstd = {self.std} \nRoll NO = {self.roll_no}")

    @classmethod
    def change_leaves_of_all(cls, newleaves):  # cls means that class which name was located
        # example:- kuldeep in students class
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # dash = string.split("-")
        # print(dash)
        # return cls(dash[0], dash[1], dash[2])
        return cls(*string.split("-"))

kuldeep = students("Kuldeep Saini", "12th Arts", "1215")
rohan = students("Rohan Verma", "12Arts", "1021")

rohan.change_leaves_of_all(4545)
print(f"After Using ClassMethods.....\n{rohan.no_of_leaves}")
karan = students.from_dash("Karan Sharma-12sci-0000")
print(karan.details())