class School:
    number_of_students = 2132

    def __init__(self, name, std, section, fees):
        self.name = name
        self.std = std
        self.section = section
        self.fees = fees

    def printdetails(self):
        print(f"\nName - {self.name}\nStd - {self.std}\nSection - {self.section}" \
               f"\nRoll_No - {self.fees}")

    def __add__(self, other):
        return self.fees + other.fees

    def __del__(self):
        return "Done"


kuldeep = School("Kuldeep", "12th", "Arts", 1215)
lovish = School("Lovish", "12th", "Arts", 1216)

print(f"\nTotal Fees:- {kuldeep + lovish}")

"""
del lovish
lovish.printdetails()
"""


# My Mind
# lovish.printdetails() or kuldeep.printdetails()
