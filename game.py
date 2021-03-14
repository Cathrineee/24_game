#!/usr/local/bin/python3
from fractions import Fraction
import random

# It finds the partial sum of cards in c


def findSum(c):
    sum = 0
    for i in c:
        sum += i
    return sum

# It finds the partial product of cards from l to r


def findMult(c):
    prod = 0
    for i in c:
        prod *= i
    return prod

# It finds the factors of goal


def findFact(goal):
    ret = [1]
    cur = 2
    while cur ** 2 <= goal:
        if (goal % cur == 0):
            ret += [cur]
            cur += 1
    return ret


def myPrint(lst):
    for x in lst:
        print(x, end=" ")
    print("\n")


class game:
    seed = 312
    cards = []
    goal = 24

    def __init__(self, seed=312):
        random.seed(seed)

    def makeCards(self):
        self.cards.append(random.randint(1, 9))
        self.cards.append(random.randint(1, 9))
        self.cards.append(random.randint(1, 9))
        self.cards.append(random.randint(1, 9))

    # This function returns the following:
    # if there are numbers between l and r in cards that can get to the goal with simple
    ## arithmetic operations, then it returns [x, '=-*/', y]
    # otherwise, it returns False
    def findGoal(self, goal, c):
        if not c:
            return False
        elif (len(c) == 1):
            if (c[0] == goal):
                return c
            else:
                return False
        elif (len(c) == 2):
            left = c[0]
            right = c[1]
            if (left + right == goal):
                return [left, '+', right]
            elif (left * right == goal):
                return [left, '*', right]
            elif (right - left == goal):
                return [right, '-', left]
            elif (left - right == goal):
                return [left, '-', right]
            elif (right % left == 0 and right // left == goal):
                return [right, '/', left]
            else:
                return False
        else:
            # if adds up to goal
            sum = findSum(c)
            if (sum == goal):
                ret = []
                for i in c:
                    ret += [i, '+']
                ret += [c[-1]]
                return ret
            # if multiply up to goal
            prod = findMult(c)
            if (prod == goal):
                ret = []
                for i in c:
                    ret += [i, '*']
                ret += [c[-1]]
                return ret
            # if there are factors of goal in the cards
            factors = findFact(goal)
            for i in c:
                if (i in factors):
                    x = i
                    y = goal // x
                    result = self.findGoal(y, c.pop(i))
                    if (result != False):
                        return [x, '*', '('] + result + [')']
            # subtract a number from goal
            for i in c:
                x = goal - i
                result = self.findGoal(x, c.pop(i))
                if (result != False):
                    return [i, '+'] + result
            # add a number to goal
            for i in c:
                x = goal + i
                result = self.findGoal(x, c.pop(i))
                if (result != False):
                    return result + ['-', i]
            # multiply goal by a number
            for i in c:
                x = goal * i
                result = self.findGoal(x, c.pop(i))
                if (result != False):
                    return ['('] + result + [')', '/', i]
        return False

    # play the 24 game!
    def gameSolution(self):
        result = self.findGoal(self.goal, self.cards)
        if (result != False):
            myPrint(result)
        else:
            print("There is no solution for the current card set.")

    # attempt is a list of player's input, check its correctness
    # paren is True if the attempt is inside a parenthesis
    # return False or a Fraction
    def calcRes(self, attempt, paren):
        if not attempt:
            return False
        curNum = False
        curOp = ''
        for i in range(len(attempt)):
            if (attempt[i] == '('):
                if (curNum != False and curOp == ''):
                    print("There are syntax errors in your input.")
                    return False
                res = self.calcRes(attempt[i+1:], True)
                if (res == False):
                    print("There are syntax errors in your input.")
                    return False
                if (curNum != False):
                    if (curOp == '+'):
                        curNum += res
                    elif (curOp == '-'):
                        curNum -= res
                    elif (curOp == '*'):
                        curNum *= res
                    else:
                        curNum /= res
                    curNum = False
                    curOp = ''
                else:
                    curNum = res
            elif (attempt[i] == '+' or attempt[i] == '-' or attempt[i] == '*' or attempt[i] == '/'):
                if (curNum == False):
                    print("There are syntax errors in your input.")
                    return False
                else:
                    curOp = attempt[i]
            elif (attempt[i] == ')'):
                if (paren == False or curOp != '' or curNum == False):
                    print("There are syntax errors in your input.")
                    return False
                else:
                    return curNum
            elif (attempt[i].isdigit()):
                if (curNum != False and curOp == ''):
                    print("There are syntax errors in your input.")
                    return False
                num = int(attempt[i])
                if (curNum == False):
                    curNum = Fraction(num, 1)
                elif (curOp == '+'):
                    curNum += num
                elif (curOp == '-'):
                    curNum -= num
                elif (curOp == '*'):
                    curNum *= num
                elif (curOp == '/'):
                    curNum /= num
            else:
                print("There are syntax errors in your input.")
                return False
        return curNum

    # It plays the 24 game
    def playGame(self):
        rounds = ''
        while True:
            try:
                rounds = input("How many rounds do you want to play?  ")
                rounds = int(rounds)
                break
            except:
                print("Invalid Integer! Please try again.")
        while True:
            try:
                self.goal = input(
                    "What's the number you want to play with? Enter a number between 20 and 60.  ")
                self.goal = int(self.goal)
                if (self.goal < 20 or self.goal > 60):
                    print("Input integer out of range! Please try again.")
                else:
                    break
            except:
                print("Invalid Integer! Please try again.")
        for i in range(rounds):
            if not self.cards:
                del self.cards[:]
                self.makeCards()
            print('Here are the cards.')
            myPrint(self.cards)
            print("You can only use +, -, *, and / as arithmetic operations.")
            print(
                "You can use parenthesis if you want, but please follow its syntax. Every characters should be ")
            print("separated by a space. Here is an example of a sample input:")
            print("1 * ( 2 + 4 ) / 3")
            print('Note that your solution should equal to {}, while the sample above equals to 2.'.format(
                self.goal))
            pIn = ''
            while True:
                try:
                    pIn = input("Please enter your solution below.\n")
                    break
                except:
                    print("Invalid input, please try again.")
            equation = []
            i = 0
            for j in range(len(pIn)):
                if (pIn[j] == ' '):
                    equation.append(pIn[i:j])
                    i = j + 1
            result = self.calcRes(equation, False)
            if (result == self.goal):
                print("Congratulations! You have found the solution.")
            else:
                print("Ohhhhh, you missed it! Here is the correct solution.")
                self.gameSolution()
        print("Good game! Bye bye~")


# start testing
myGame = game()
myGame.playGame()
