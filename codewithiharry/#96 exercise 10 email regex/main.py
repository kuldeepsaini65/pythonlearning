import re

strr = '''
here is cool boy k.deep saini coolboyk.deepsaini@gmail.com sahil khurana ka email itz_sahil.saini0065@gmail.org
and sainikuldeep@gmail.com and tricksandclips@trickindia.com terabhai@gmail.com
'''

finding = re.findall('\S+@\S+',strr)
a = 0
for i in finding:
    a = a+1
    print(f"Email{a}:- {i}")

