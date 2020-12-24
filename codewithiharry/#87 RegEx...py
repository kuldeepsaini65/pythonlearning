import re

# Findall()

# aq = re.compile(r'my') # match All Char left \n
# d = aq.findall(aa)
# for match in d:
#     print(match)
# print(d)


# Search()
# aa = "hello my frnd my name is kuldeep saini and how are you my baby"
# ss = re.search('hello', aa)
# print(ss)


# names = 'kuldeep lalit lovish saini and no one'
# r = re.search('saini',names)
# print(r)


#split
# string = 'kuldeep and lovish and rohit and deep and saini and kuta raghav'
# splt = re.split('and', string)
# for i in splt:
#     print(i)


# Sub()
# strings = 'kuldeep and is great and is powerfull and is famous'
# subs = re.sub('and', ' saini',strings)
# print(subs)


# Finditer()
#
# s = "Hello my frnd how are you my name is kuldeep"
# r = re.compile('my')
# dd = r.finditer(s)
# for i in dd:
#     print(i)
#
# s = "Hello my frnd how are you my name is kuldeep"
# x = re.compile('my')
# a = x.finditer(s, 8, 25)
# for i in a:
#     print(i)
#
# print(s[6:8])


# s = 'hello my name is kuldeep and my dob'
# res = re.finditer('my', s)
# for i in res:
#     print(i)


# string = 'hello my name is kuldeep saini and today i will tell you ' \
#         'ow you can easily hack someone computer and today this is last video' \
#          'about hacking aabiut hheello ai aiii aaii aiai @22 #33 aaaii'
# rew = re.compile('.')
# rew = re.compile('^hello')
# rew = re.compile('hacking$')
# rew = re.compile('abo*')
# rew = re.compile('hel+')
# rew = re.compile('he{1}')
# rew = re.compile('(ai) {1}')

# string = 'kuldeep saini is learning python. python is popular amoung us. kuldeep saini is beginner'
# a = re.finditer('a+',string)
# for i in a:
#     print(i)


# finding a number or a string from a given string
# roll_no = 'rahul 1202 kuldeep 1204 lovish 1202'
# ree = re.findall('[0-9]+',roll_no)
# az = re.findall('[a-z]+',roll_no)
# for i in ree,az:
#     print(i)

# testing purpose
# students = 'kuldeep saini Kuldeep Lovish rahul PARAS 232'
# aq = re.findall('[A-z]+',students)
# for i in aq:
#     print(i)

string = '8865 9565 5565 0065'
ww =re.findall('[0-9]+',string)
print(ww)