food_lists= ['apple','banana','mango','cherry']
print('------First Method------')
a = food_lists[::-1]
print(a)

print('------Second Method------')
fod_lst= ['apple','banana','mango','cherry']
fod_lst.reverse()
print(fod_lst)
print('------Third Method-------')
for i in range(len(food_lists)//2):
       food_lists[i],food_lists[len(food_lists)-i -1] = food_lists[len(food_lists) -i -1] ,food_lists[i]

print(food_lists)
