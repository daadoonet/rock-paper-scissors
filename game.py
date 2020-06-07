import sys
import os
import random

os.system('cls')


# defines the game logic
def logic(p1, p2):
    # checks if the input is valid or not
    if not ((p1 == "1" or p1 == "2" or p1 == "3") and (p2 == "1" or p2 == "2" or p2 == "3")):
        print("something went wrong")
        main()
    else:
        if p1 == p2:
            print("that's a tie ...")

        if p1 == "1":
            if p2 == "2":
                print("player2 wins!!")
            elif p2 == "3":
                print("player1 wins!!")

        if p1 == "2":
            if p2 == "1":
                print("player1 wins!!")
            elif p2 == "3":
                print("player2 wins!!")

        if p1 == "3":
            if p2 == "1":
                print("player2 wins!!")
            elif p2 == "2":
                print("player1 wins!!")


# deletes the previous line
def deleteLine():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


# asks for play again or exit
def exit():
    playAgain = input(" \ndo you want to play again ? y/n \n")
    if playAgain == "y":
        os.system('cls')
        main()
    elif playAgain == "n":
        sys.exit()
    else:
        exit()


def main():

    print("""
    ###################
    ##               ##
    ##  1. rock      ##
    ##  2. paper     ##
    ##  3. scissors  ##
    ##               ##
    ###################
    """)

    # asks for game mode
    gameMode = input("multiplayer or single player? m/s \n").lower()

    if gameMode == "m":

        # gets palyers moves
        player1 = input("player 1 choose your move number:  ").lower()
        deleteLine()
        player2 = input("player 2 choose your move number:  ").lower()
        deleteLine()

        logic(player1, player2)
        exit()

    elif gameMode == "s":
        # gets palyers moves
        player1 = input("player 1 choose your move number:  ").lower()
        deleteLine()
        player2 = str(random.randint(1, 3))
        print(f"Computer move was: {player2}")

        logic(player1, player2)
        exit()
    else:
        os.system('cls')
        main()


# runs the program
main()
