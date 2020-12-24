import time

# to find program execution time
"""
a = time.time()
for i in range(1000):
    print(i)

print(f"Time of For loop = {time.time() - a}")

bb = time.time()
x = 0
while x < 1000:
    print(x)
    x += 1

print(f"Time of While Loop = {time.time() - bb}")

"""

#to print Time with All info Like day,time,month,year
time_date = time.asctime()
print(time_date)
print(time.gmtime())