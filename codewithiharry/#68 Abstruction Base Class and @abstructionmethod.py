from abc import abstractmethod, ABC
# This wil Implement Rule to child Class

""" Shape Is a Parent Class And It Has It Rule To Define Print_Area """


class Shape(ABC):
    @abstractmethod
    def print_area(self):
        pass    # or return 0
    # We can't create object into this ex:- harry = Shape()

class Rectangluar(Shape):
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.hight = 2
        self.weidth = 4

    def print_area(self):
        return self.hight * self.weidth


rohan = Rectangluar()
print(rohan.print_area())
