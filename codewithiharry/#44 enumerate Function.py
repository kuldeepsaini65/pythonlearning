# list of Material to buy :- Example
# it is first method

# list_for_jarvis = ["Bhindi", "Chinni", "Loki", "Kadu"]
# i = 1
# print()
# for items in list_for_jarvis:
#     if i % 2 != 0:
#         print(f"Jarvis Please Bring {items}")
#     i += 1



# 2nd Method with enumerate function
# it will give index and items

list_for_jarvis = ["Bhindi", "Chinni", "Loki", "Kadu"]
for index, items2 in enumerate(list_for_jarvis):
    if index % 2 == 0:
        print(f"Jarvis go and buy {items2}")
