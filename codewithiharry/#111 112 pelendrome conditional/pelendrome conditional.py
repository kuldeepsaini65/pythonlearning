'''

Author - Kuldeep Saini
Purpose - Learning Python
Instagram - https://www.instagram.com/kuldeep_saini_65
License - Free to Use, Edit, Distribute ;-)

'''

lst = [2,20,6,10,20,40,54]


def next_pelendrome(number):
    return str(number) == str(number)[::-1]

def not_pelendrome(number):
    if number<10:
        pass
    else:
        while not next_pelendrome(number):
            number = number+1
        return number

for findinf_lst in range(len(lst)):
    if lst[findinf_lst] <10:
        pass
    else:
        if not_pelendrome(lst[findinf_lst]) == None:
            pass
        else:
            print(f'The Pelendrome Number of {lst[findinf_lst]} is {not_pelendrome(lst[findinf_lst])}')