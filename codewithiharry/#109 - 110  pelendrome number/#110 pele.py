def next_peledrome(n): # this function will find next peledrome number if not then add
    # the number until it peledrome
    n = n+1
    while not is_peledrome(n):
        n = n+1
    return n

def is_peledrome(n): # this will tell is this peledrome or not by true false
    return str(n) == str(n)[::-1]

if __name__ == '__main__':

    numbers = []
    n = int(input("How much Pelindrome You Want To Know:- "))
    for i in range(n):
        number = int(input("Enter Your Number:-  "))
        numbers.append(number)


    for returning_pele in range(n):
        print(f'the Pelendrome number of {numbers[returning_pele]} is {next_peledrome(numbers[returning_pele])}')



