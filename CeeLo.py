import time
import os
import platform
import sys
from functools import reduce

players = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5']

roll_val = {'0':0, '123':1, '1':2, '2':3, '3':4, '4':5, '5':6, '6':7, '111':8, '222':9, '333':10, '444':11, '555':12, '666':13, '456':14}
roll_display = {0:'No Score', 1:'One Two Three', 2:'1', 3:'2', 4:'3', 5:'4', 6:'5', 7:'6', 8:'Trip Ones', 9:'Trip Twos', 10:'Trip Threes', 11:'Trip Fours', 12:'Trip Fives', 13:'Trip Sixes', 14:'Four Five Six'}
round_display = {0:'Init', 1:'First Round', 2:'Overtime', 3:'Double Overtime', 4:'Triple Overtime'}

class Player:
    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__theround = 0

    def __str__(self):
        return self.__name

    def setscore(self, score):
        self.__score = score

    def getscore(self):
        return self.__score

    def getscoredisplay(self):
        return roll_display[self.__score]

    def settheround(self, theround):
        self.__theround = theround

    def gettheround(self):
        return self.__theround

    __repr__ = __str__



def StartGame():
    rollers = []

    for player in players:
        newroller = Player(player)
        rollers.append(newroller)

    while True:
        if len(rollers) > 1:
            rollers = StartRound(rollers)
        else:
            EndGame(rollers)





def StartRound(rollers):
    for roller in rollers:
        roller.setscore(0)
        roller.settheround(roller.gettheround() + 1)
    currenthighscore = 0

    for roller in rollers:
        ClearTheScreen()
        currentrollscore = 0
        print(GetRoundDisplay(roller.gettheround()))
        print("{0} is the score to beat".format(roll_display[currenthighscore]))
        print("{0} is currently rolling".format(roller))
        currentrollscore = roll_input()
        roller.setscore(currentrollscore)
        if currentrollscore > currenthighscore:
            currenthighscore = currentrollscore

    rollers = TrimLosingRollers(rollers)

    return rollers


def FindHighScore(rollers):
    scores = []

    for roller in rollers:
        scores.append(roller.getscore())

    f = lambda a, b: a if (a > b) else b
    highscore = reduce(f, scores)

    return highscore


def TrimLosingRollers(rollers):
    trimhighscore = FindHighScore(rollers)
    trimmedrollers = [roller for roller in rollers if roller.getscore() >= trimhighscore]
    return trimmedrollers


def roll_input():

    while True:
        try:
            choice = input("Enter the Roll: ")
            if choice in roll_val:
                rollscore = roll_val[choice]
                break
            else:
                print("Invalid Choice...Enter a valid CeeLo Roll")
                print("Valid Rolls are 0 123 1 2 3 4 5 6 111 222 333 444 555 666 456")
                time.sleep(4)
                raise Exception('Invalid Choice...')
        except:
            continue

    return rollscore

def ClearTheScreen():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    return


def EndGame(rollers):
    ClearTheScreen()
    print("{0} is the winner with a score of {1} ".format(rollers[0], roll_display[rollers[0].getscore()]))
    sys.exit()

def GetRoundDisplay(roundindex):
    if roundindex > 4:
        prettyround = "End it Already!!!"
    else:
        prettyround = round_display[roundindex]
    return prettyround




StartGame()
