# Diamond Shaped Problem Means :- confusion Which Class use Which method
class A:
    def met(self):
        print("This is from Class A")


class B(A):
    def met(self):
        print("This is from Class B")


class C(B):
    def met(self):
        print("This is from Class C")


class D(C, B):
    def met(self):
        print("This is from Class A")


a = A()
b = B()
c = C()
d = D()

d.met()