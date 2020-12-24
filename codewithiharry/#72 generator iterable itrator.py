"""
Iterable = __iter__() or __getitem__()
iterator = __next__()
iteration =

"""

"""
Generator-Function : A generator-function is defined like a normal function,
but whenever it needs to generate a value, it does so with the yield keyword rather than return.
If the body of a def contains yield, 
the function automatically becomes a generator function.
"""

"""
Fibonacci Series:-  0+1=1+2=3+5=8..... And So On 
"""

"""
#simple generator yield is impo.
def test(limit):
    for i in range(limit):
        yield i


x = test(12)
print(x.__next__())
print(x.__next__())
"""

"""
#fabnacii series 
def gen1(number_limit):
    a, b = 0, 1
    while a <= number_limit:
        yield a
        a, b = b, a + b


print("Using for loop")
for i in gen1(12):
    print(i)

print("Without using For loop")
print("")
x = gen1(45)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
"""


# Factorial Number series
#
# def factgen(user):
#     factorial = 1
#     if user < 0:
#         print("Oops ! Can't provide Factorial number of negative number")
#     elif user == 0:
#         print("The Factorial of 0 is 1")
#     else:
#         for i in range(1, user + 1):
#             factorial = factorial * i
#
#     yield f"{factorial} this is factorial of {value}"
#
#
# value = int(input("Enter your Number:- "))
# print(factgen(value).__next__())
# print(factgen(13).__iter__())


#iter
# a = "HARRY"
# ier = iter(a)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())

"""***** Using For Loop ******"""
# a = "HARRY"
# for i in a:
#     print(i)