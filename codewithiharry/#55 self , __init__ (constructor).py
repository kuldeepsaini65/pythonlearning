# To Understanding this must Watch Video #55 self init

class students:
    def __init__(self, name, std, rollno):  # Constructor
        self.name = name
        self.std = std
        self.roll_no = rollno

    def details(self):
        print(f"Name = {self.name} \nstd = {self.std} \nRoll NO = {self.roll_no}")


kuldeep = students("Kuldeep Saini", "12th Arts", "1215")
print(kuldeep.details())
