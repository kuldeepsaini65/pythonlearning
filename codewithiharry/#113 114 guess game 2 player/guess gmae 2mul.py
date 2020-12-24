"""
This Code Is Developed By Kuldeep Saini
My Instagram:-  https://www.instagram.com/kuldeep_saini_65

This Is A Guess Game Of 2 Players. Both Player Must Guess A Correct Number In Less Chances then Other Player
Language Used:-  Python

I Used Basic Python Concept To Build This Game
"""

from random import randint  # By Importing This We Will Randomly Chose a Number as a Actual Number


def guessgame(starting_number, last_number, actual_number):
    number_of_guess = 1
    player_guess = int(input(f'PLease Enter your Guess Number Between {starting_number} and {last_number} :- '))

    while player_guess != actual_number:  # until the player guess didn't match with the actual number loop keeps going

        if player_guess < actual_number:
            player_guess = int(input(f'You Entered Smaller Number Then Acutal Number. Plaese Guess Again Between {starting_number} and {last_number} :- '))
            number_of_guess = number_of_guess + 1

        else:
            player_guess = int(input('\nEnter a Smaller Number:- '))
            number_of_guess = number_of_guess + 1

        # We Didn't Give The Third Situation Of When player_guess == actual_Guess, bcz it is alerdly defined in While
        # Loop if this situation happen then player 2 turns come

    print(f'Your Guessed correct number in {number_of_guess} Guesses')
    return number_of_guess  # This is Important Because This Will Tell Player Used How Much Guess and number of less
    # guesses will win the game


if __name__ == "__main__":
    starting_number = 0
    last_number = 2
    actual_number = randint(starting_number, last_number)

    print('------ Player 1 Turn ------\n')
    player1 = guessgame(starting_number, last_number, actual_number)

    print('\n-------- Player 2 Turns ---------\n')
    player2 = guessgame(starting_number, last_number, actual_number)

    print('---------- R E S U L T S -------------')
    if player1 < player2:  # this will compare number_of_guesses
        print('Player 1 Won The Guess Game ')
    elif player1 > player2:
        print('Player 2 Won The Guess Game ')
    else:
        print('TIE!  Player 1 And Player 2 Score Are Same')
