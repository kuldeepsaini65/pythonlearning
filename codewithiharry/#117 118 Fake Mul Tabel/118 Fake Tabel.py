from random import randint


def rohanDasProgramme(value):
    listfortabel = []    # Created for Inserting Tabel into it

    for i in range(1, 11):  # creating tabel
        a = value * i
        listfortabel.append(a)

    fraudTabel = listfortabel[fraudNumber] = fraudNumber + fraudNumber  # Now Changing One Random Number With 2x of Random number
    return listfortabel


def corrector(value):
    correct_tabel_list = []     # Created for Inserting Tabel into it

    fake_tabel = rohanDasProgramme(value)  # For Comparing RohanDasProgramme With Our Corrector Function

    for correct_tabel in range(1, 11):      # Generating Correct Tabel
        tabel = value * correct_tabel
        correct_tabel_list.append(tabel)

    for i in range(0, 10):     # If Any Multiplication Tabel Number Found Then It Will Replace it With " W "
        if correct_tabel_list[i] == fake_tabel[i]:
            pass
        elif correct_tabel_list[i] != fake_tabel[i]:
            fake_tabel[i] = 'W'
            print(f'{correct_tabel_list[i]} Is At " W " Place')

    return fake_tabel


if __name__ == '__main__':
    user_input = int(input("Please Enter your Number :- "))     # Taking User Number To Generate User Desired Tabel

    print('Processing.....   Sending Data to Rohan Das')
    fraudNumber = randint(5, 9)  # Used In RohanDasProgramme To Replace One Random Number With One 2xRandom Number
    print(rohanDasProgramme(user_input))

    print('\nSending Data To Corrector........')
    print(corrector(user_input))

    print('Hence Proved ! Rohan Das Is a Fraud')

