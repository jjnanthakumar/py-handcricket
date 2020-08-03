#                       *************** Author: -> Nanthakumar J J *****************
'''THIS CODE IS CREATED BY NANTHAKUMAR J J U CAN USE THIS CODE AND MODIFY BUT DONT FORGOT TO GIVE CREDITS TO https://jjnanthakumar.github.io/'''
'''#FEEL FREE TO CONTACT ME IF ANY ERROR OCCURS#'''
#HAVE FUN


import random, sys


def h_batting(runs=None):
    h_score = 0
    print("Ready to Rock....")
    while (True):
        try:
            n = int(input("Enter a number between 1- 10: -> "))
        except ValueError:
            print("Oops! Input must be integers..")
            choice = input("Type yes or no to continue or exit: -> ")
            if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'y':
                continue
            else:
                return "*****************Thanks for playing******************"

        if n <= 10 and n > 0:

            r = random.randint(1, 10)
            if n == r and h_score == 0:
                print("*******Duck Out!*********")
                return 0
            h_score += n
            if n == r:
                print("Oops! *******Out!******* ")
                return h_score
            else:

                print("You scored {} runs".format(h_score))
            if runs != None and h_score >= runs:
                return c_score

        else:
            print("Oops! U entered an invalid input which is against game rules...")
            choice = input("Type yes or no to play again or exit: -> ")
            if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'y':
                continue
            else:
                return "**********************Thanks for playing*************************"


def h_bowling(runs=None):
    c_score = 0
    print("Ready for bowling.........")
    while (True):
        try:
            n1 = int(input("Enter a number between 1- 10: -> "))
        except ValueError:
            print("Oops! Input must be integers..")
            choice = input("Type yes or no to continue or exit: -> ")
            if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'y':
                continue
            else:
                return "*****************Thanks for playing******************"
        if n1 <= 10 and n1 > 0:
            r = random.randint(1, 10)
            if n1 == r and c_score == 0:
                print("Excellent! ***********Machine Duck Out***********")
                return 0
            c_score += r
            if n1 == r:
                print("Good ! You took wicket.. ")
                return c_score
            else:
                print("Computer scored {} runs".format(c_score))
            if runs != None and c_score >= runs:
                return c_score
        else:
            print("Oops! U entered an invalid input which is against game rules...")
            choice = input("Type yes or no to play again or exit: -> ")
            if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'y':
                continue
            else:
                return "**********************Thanks for playing*************************"


def finalresult(h_score, c_score, name):
    print("Your Final Score is: " + str(h_score) + " ---------- > " + "Machine Final Score is: " + str(c_score))
    if h_score > c_score:
        print("Congragulations " + name.upper() + " You Won the match against machine! in the difference of " + str(
            h_score - c_score) + ' runs')
    elif h_score == c_score:
        print("**********Match Draw***********")
    else:
        print("Oops! sorry {} Better luck next time Machine Won the match.... by {} runs".format(name.upper(), abs(
            c_score - h_score)))


print("********Hand Cricket Game versus Machine**********")
name = input("Enter your name: ")
try:
    if type(name) != str:
        raise Exception
    if int(name):
        sys.exit("Oops! Please Provide a valid name..")
except ValueError:
    pass
except Exception:
    sys.exit("Oops! Please Provide a valid name..")
print("Welcome to Handcricket Game Mr/Ms/Mrs. " + name.upper())
h_score, c_score = 0, 0
c_dict = {1: 'odd', 2: 'even'}
c_batorbowl = {1: 'batting', 2: 'bowling'}
ur_toss = input("Choose odd or even for tossing: --> ")
try:
    if type(ur_toss) != str or ur_toss != 'odd' and ur_toss != 'even':
        raise Exception
    if int(ur_toss):
        sys.exit("Oops! Please Provide a valid input..")
except ValueError:
    pass
except Exception:
    sys.exit("Oops! Please Provide a valid input..")
ur_toss = ur_toss.lower()
c_toss = random.randint(1, 2)
power = ''
if (ur_toss == 'even' and c_dict.get(c_toss) == 'odd') or (ur_toss == 'odd' and c_dict.get(c_toss) == 'even'):
    c_toss_num = random.randint(1, 100)
    try:
        h_toss_num = int(input("Please enter any number for even or odd toss : "))
    except:
        sys.exit("Oops! Input must be integers only..")
    if (h_toss_num & 1 and ur_toss == 'odd') or (h_toss_num % 2 == 0 and ur_toss == 'even'):
        print("********Hurray! You won toss*********")
        power = 'human'
    else:
        print("*****Oops! You lost the toss Better luck next time*****")
        power = 'machine'
else:
    print("*****Oops! You and machine choosed same toss*****")
    print("But machine accepts ur wish and machine will take opposite of you...")
    if ur_toss == 'even':
        c_toss = 'odd'
    else:
        c_toss = 'even'
    c_toss_num = random.randint(1, 100)
    try:
        h_toss_num = int(input("Please enter any number for even or odd toss : "))
    except ValueError:
        sys.exit("Oops! Input must be an integer..")
    if (h_toss_num & 1 and h_toss_num == 'odd') or (h_toss_num % 2 == 0 and h_toss_num == 'even'):
        print("********Hurray! You won toss*********")
        power = 'human'
    else:
        print("*****Oops! You lost the toss Better luck next time*****")
        power = 'machine'
if power == 'human':
    c = input("You can choose either batting or bowling: -> ")
    try:
        if type(c) != str or c != 'batting' and c != 'bowling' and c != 'bat' and c != 'bow':
            raise ValueError
        if int(c):
            sys.exit("Oops! Please Provide a valid input..")
    except ValueError:
        pass
    except Exception:
        sys.exit("Oops! Please Provide a valid input..")
    if c == 'batting' or c == 'bat':
        print("Finally.. You choosed Batting" + " --------------- > " + "Computer chooses Bowling")
        h_score = h_batting()
        if type(h_score) == int:
            print("You Scored: " + str(h_score) + " runs ")
            c_score = h_bowling(h_score)
            finalresult(h_score, c_score, name)
        else:
            print(h_score)

    elif c == 'bowling' or c == 'bow':
        print("Finally.. You choosed Bowling" + " --------------- > " + "Computer chooses Batting")
        c_score = h_bowling()
        if type(h_score) == int:
            print("Computer Scored: " + str(c_score) + " runs ")
            print("Your target is: --> " + str(c_score + 1)+' runs')
            h_score = h_batting(c_score)
            finalresult(h_score, c_score, name)
        else:
            print(h_score)
else:
    x = random.randint(1, 2)
    if c_batorbowl.get(x) == 'batting':
        print("Computer Choosed batting" + " ------------------ > " + "Then You chooses bowling")
        c_score = h_bowling()
        if type(c_score) == int:
            print("Computer Scored: " + str(c_score) + " runs ")
            print("Your target is: --> " + str(c_score + 1)+' runs')
            h_score = h_batting(c_score)
            finalresult(h_score, c_score, name)
        else:
            print(c_score)
    elif c_batorbowl.get(x) == 'bowling':
        print("Computer Choosed bowling" + " ------------------ > " + "Then You chooses batting")
        h_score = h_batting()
        if type(h_score) == int:
            print("You Scored: " + str(h_score) + " runs ")
            c_score = h_bowling(h_score)
            finalresult(h_score, c_score, name)
        else:
            print(h_score)




#                       *************** Author: -> Nanthakumar J J *****************
