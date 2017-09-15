'''Work on generating a random number and color first.'''

import random

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

greenNums = [0, 37]
blackNums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
redNums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


def takeBet():
    userBetChoice = ''
    while not userBetChoice == "color" and not userBetChoice.isdigit():
        userBetChoice = raw_input("Make a Bet!\nEnter a number between 0 and 37, or 00 (enter 'color' to just pick a color): ")
    if userBetChoice == "color":
        while not userBetChoice == "black" and not userBetChoice == "red" and not userBetChoice == "green":
            userBetChoice = raw_input("Enter a color ('black' , 'red' , 'green')")
    return userBetChoice


def roll_ball():
    ballLandNumber = random.randint(0, 37)
    if ballLandNumber in blackNums:
        ballColor = "black"
    elif ballLandNumber in redNums:
        ballColor = "red"
    else:
        ballColor = "green"
    return([ballLandNumber, ballColor])


def checkResults():
    pass


def payout():
    '''payout for colors vs numbers'''
    pass


def play_game():
    print(takeBet())
    print(roll_ball())


play_game()
