import random
import time
import sys

greenNums = [0, 37]
blackNums = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
redNums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


def takeBet():
    userBetMoney = ''
    userBetChoice = ''
    while not userBetMoney.isdigit():
        userBetMoney = raw_input("How much are you going to bet: $")
    while not userBetChoice == "color" and not userBetChoice.isdigit():
        userBetChoice = raw_input("Enter a number between 0 and 37 (enter 'color' to just pick a color): ")
    if userBetChoice == "color":
        while not userBetChoice == "black" and not userBetChoice == "red" and not userBetChoice == "green":
            userBetChoice = raw_input("Enter a color ('black' , 'red' , 'green'): ")
        userBetChoice = userBetChoice[0].upper() + userBetChoice[1:]
    return [userBetChoice, userBetMoney]


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
    print("========================")
    print("Ball Landed on " + ballLandArr[1] + " " + str(ballLandArr[0]))
    print("You Chose " + userBetChoice[0])
    print("Your Bet: $" + userBetChoice[1])
    if userBetChoice[0].isdigit() and int(userBetChoice[0]) == ballLandArr[0]:
        payout("numWin", userBetChoice[1])
    elif not userBetChoice[0].isdigit() and userBetChoice[0] == ballLandArr[1]:
        payout("colorWin", userBetChoice[1])
    else:
        payout("lose", userBetChoice[1])
    print("========================")



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


def payout(caseString, userBetMoney):
    if caseString == "numWin":
        print("You Win $" + str((int(userBetMoney)*3)) + "!")
    if caseString == "colorWin":
        print("You Win $" + str((int(userBetMoney)*0.50)) + "!")
    else:
        print("You Lose $" + userBetMoney)



def play_game():
    checkResults(takeBet(), roll_ball())

play_game()
