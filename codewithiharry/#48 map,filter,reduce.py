"""
Index
to find press crtl + F
"""

# Map function is used to typecast string or number in One line

# list of a string numbers
numbers = ["34", "12", "22", "34"]

# TypeCasting A string in integer without Map function
"""
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers = numbers[2] + 3
print(numbers)
"""

# TypeCasting string to int with map function
"""
numbers = list(map(int, numbers)) # Here List is used to typecaste in list
                  # What to Apply on All, Where to apply these
numbers = numbers[2] + 1
#          position of number + how much to add
print(numbers)
"""

# Finding Square of number With map and function/lambda
"""
exmpl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# Using Function() with Map
def sqar(x):
    return x * x
"""

"""
sqfun = list(map(sqar, exmpl))
print(sqfun)
# Using lambda in Map function
sqr = list(map(lambda x: x * x, exmpl))
print(sqr)
"""


# cube with map and function

def square(x):
    return x * x


def cube(x):
    return x * x * x


exmplr_cube = [1, 2, 3, 4, 5, 6]
func = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

# --------------- FILTER -----------------

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
final = list(filter(lambda num: num > 5, list_1))
print(final)
# here we finded number that were grater than 5 and printed them

# --------------- REDUCE -----------------

from functools import reduce

a = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, a)
print(sum)
