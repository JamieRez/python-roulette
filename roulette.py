'''Work on generating a random number and color first.'''

import random
import time
import sys

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
            userBetChoice = raw_input("Enter a color ('black' , 'red' , 'green'): ")
        userBetChoice = userBetChoice[0].upper() + userBetChoice[1:]
    return userBetChoice


def roll_ball():
    ballLandNumber = random.randint(0, 37)
    if ballLandNumber in blackNums:
        ballColor = "Black"
    elif ballLandNumber in redNums:
        ballColor = "Red"
    else:
        ballColor = "Green"
    return([ballLandNumber, ballColor])


def checkResults(userBetChoice, ballLandArr):
    loadBar()
    print("Done!")
    print("Ball Landed on " + ballLandArr[1] + " " + str(ballLandArr[0]))
    print("You chose " + userBetChoice)


def loadBar():
    print("Rolling the Ball!")
    for i in range(0, 4):
        loadingString = ""
        sys.stdout.write('\x1b[2K')
        for j in range(0, 8):
            time.sleep(0.05)
            loadingString += "~"
            sys.stdout.write("\r" + loadingString)
            sys.stdout.flush()
    sys.stdout.write('\x1b[2K')


def payout():
    '''payout for colors vs numbers'''
    pass


def play_game():
    checkResults(takeBet(), roll_ball())



play_game()
