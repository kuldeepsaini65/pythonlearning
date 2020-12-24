"""
Age Calculator
Supported Birth Year - 1941 to 2019
Calculate Year Up to -
"""

birth_year = int(input("Enter your Birth Year (Ex- 1970, 2003):- "))
if birth_year <= 1940:
    print('It seems that, You Are only Oldest person on the Earth')
elif birth_year >= 2021:
    print('It Seems that this person Not Yet Born')
else:
    present_age = (2020 - birth_year)
    option = input(f"{present_age} Is Your Current Age? Yes/No :- ").capitalize()
    if option == 'Yes':
        print('Thanks For Conform\n')
    elif option == 'No':
        print('Sorry For Our Mistake!\nPlease Give Us Feedback to Improve our Program\nFeedback on - https://www.instagram.com/kuldeep_saini_65')
        exit()

    target_year = int(input("Enter Which Year You Want To Know Your Age:- "))
    if target_year == 2020:
        print('Mr.KoiBhi, You Entred Current Year')
    elif target_year<2019:
        print("Sorry We Don't like To Give you this Result. Please Enter another Year")
    elif target_year >= 3000:
        print(f"I think You Should Not Take Too Much Tension about Your Age in {target_year}")
    else: print(f"Your Age In {target_year} is {target_year - birth_year}")
