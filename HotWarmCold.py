#HotWarmCold logic game founded by Al Sweigart, my Python teacher

import random, sys

maxguess = 10
digits = 3

# here are the rules of the game
rules ='''I am thinking of a {}-digit number. There is no digit duplicate.
Pay attention! eg: 037 can be a number as well!
Try to guess what the number is. Here are some clues:

When I say:    That means:
  Warm         One digit is correct but in the wrong position.
  Hot          One digit is correct and in the right position.
  Cold         No digit is correct.

I have thought up my number.
You have {} guesses to get it. Good luck!'''.format(digits,maxguess)

print('Hello. What is your name?')  #intro to get to know player
name = input()
print('Hi ' + name + '! Nice meeting you :)')

print(rules)     #game rules printed


def hotwarmcold():  #the game itself
    GoalNum = ''
    numbers = list('0123456789')    #these digits can be choosen
    random.shuffle(numbers)         #shuffled into random order
    for i in range(digits):
        GoalNum += numbers[i]   #random X digit number given defined by "digits" value
        

    for j in range(1, maxguess + 1):
        guess = input()
        
        while len(guess) != digits or not guess.isdecimal():
            print('Typed value is not a {} digit number'.format(digits))    #input validation check
            guess = input()

        if guess == GoalNum:            #winning condition
            break

        clues = []                      #listing out clues
        for k in range(digits):
            if guess[k] == GoalNum[k]:  #digit in correct position (Hot)
                clues.append('Hot')

            elif guess[k] in GoalNum:   #digit is in the GoalNum, but not correct position (Warm)
                clues.append('Warm')

        if len(clues) == 0:             #no digit in GoalNum (Cold)
            clues.append('Cold')

        clues.sort()
        print(clues)

    if guess == GoalNum:    #winnig statement
        print('Well done! The number I was thinking of was ' + GoalNum + '. It took you ' + str(j) + ' guesses to find out.')
    else:                   #loop ended before finding out number, loose statement
        print('The number was: ' + GoalNum)

    print('''Type "yes" if you want to play again''')   #restart game if user wants to
    if input() == 'yes':
        print('I have tought up my new number')
        hotwarmcold()
    else:   #end program if user says so
        sys.exit()
      
hotwarmcold()