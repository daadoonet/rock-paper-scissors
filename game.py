import sys
import os
import random

os.system('cls')


# defines the game logic
def logic(p1, p2, mode):
    #set outputs
    if mode == "m":
        w1 = "player1 wins!!"
        w2 = "player2 wins!!"
    elif mode == "s":
        w1 = "you win :)"
        w2 = "computer wins :("

    # checks if the input is valid or not
    if not ((p1 == "1" or "2" or "3") and (p2 == "1" or "2" or "3")):
        print("something went wrong")
        main()
    else:
        #TODO make if's shorter
        if p1 == p2:
            print("that's a tie ...")

        if p1 == "1":
            if p2 == "2":
                print(w2)
            elif p2 == "3":
                print(w1)

        if p1 == "2":
            if p2 == "1":
                print(w1)
            elif p2 == "3":
                print(w2)

        if p1 == "3":
            if p2 == "1":
                print(w2)
            elif p2 == "2":
                print(w1)


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

        logic(player1, player2, "m")
        exit()

    elif gameMode == "s":
        # gets palyers moves
        player1 = input("player 1 choose your move number:  ").lower()
        deleteLine()
        player2 = str(random.randint(1, 3))
        print(f"Computer move was: {player2}")

        logic(player1, player2, "s")
        exit()
    else:
        os.system('cls')
        main()


# runs the program
main()

#TODO add point counter
