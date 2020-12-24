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
        return cls(*string.split("-"))

    @staticmethod  # This will Help to Create A simple Function Without self or cls
    def printname():
        return print("Tera bhai cool hai")


class programmer(students):  # it means a new class with old class function
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def proginfo(self):
        print(f"Name Is {self.name}\nSalary is {self.salary}\nRole is {self.role}")


kuldeep = students("Kuldeep Saini", "12th Arts", "1215")
rohan = students("Rohan Verma", "12Arts", "1021")

# students.printname()
# kuldeepsaini = students("Kuldeep Saini", "12th", "1219")
# kuldeepsaini.details()

kuldeep = programmer("kuldeep", 12000, "developer")
kuldeep.proginfo()


