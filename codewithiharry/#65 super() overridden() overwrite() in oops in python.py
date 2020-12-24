# for this Watch Video
class A:
    classvar1 = "I Am in Var 1 in Class A"

    def __init__(self):
        self.var1 = "Inside in Class A "
        self.classvar1 = "i am a class variable in class A"
        self.special = "Special in class A"


class B(A):
    classvar1 = "I Am in Class B"
    def __init__(self):
        super().__init__()  # it will call class A all elements after than it will call class B overwritten elements
        self.var1 = "Inside in Class B "
        self.classvar1 = "i am a class variable in class B"
        # super().__init__() # it will call Class A all elements


a = A()
b = B()

print(b.special, b.classvar1, b.var1)