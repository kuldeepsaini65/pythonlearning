class students:
    no_of_leaves = 400  # public
    _protected = 10000000000000000  # protected
    __private = 999999999999999999999999999999999   #private

    def __init__(self, name, std, rollno):  # Constructor
        self.name = name
        self.std = std
        self.roll_no = rollno

    def details(self):
        print(f"Name = {self.name} \nstd = {self.std} \nRoll NO = {self.roll_no}")


kuldeep = students("Kuldeep Saini", "12th Arts", "1215")
class testing(students):
    okkk = 90
    print(kuldeep._protected)
    print(kuldeep._students__private)

print(kuldeep._protected)
