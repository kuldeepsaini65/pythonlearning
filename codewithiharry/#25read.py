d= open("kuldeep.txt.txt")

# print(d.readline()) # Only Read first line
# print(d.read())
for line in d:
    print(line, end=" ")

#print("1", d)
d.close()
