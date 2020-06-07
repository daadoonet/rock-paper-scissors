import sys
import os

os.system('cls')


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

    # deletes the previous line
    def deleteLine():
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

    # gets palyers moves
    p1 = input("player 1 choose your move number:  ")
    deleteLine()
    p2 = input("player 2 choose your move number:  ")
    deleteLine()

    # checks if the input is valid or not
    if not ((p1 == "1" or p1 == "2" or p1 == "3") and (p2 == "1" or p2 == "2" or p2 == "3")):
        print("something went wrong")
        main()
    else:
        if p1 == p2:
            print("that's a tie ...")

        if p1 == "1" and p2 == "2":
            print("player2 wins!!")
        elif p1 == "1" and p2 == "3":
            print("player1 wins!!")

        if p1 == "2" and p2 == "1":
            print("player1 wins!!")
        elif p1 == "2" and p2 == "3":
            print("player2 wins!!")

        if p1 == "3" and p2 == "1":
            print("player2 wins!!")
        elif p1 == "3" and p2 == "2":
            print("player1 wins!!")

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

    # runs exit function
    exit()


# runs the program
main()
