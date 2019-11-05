import random

CONST_LOW_NUMBER = 1
CONST_HIGH_NUMBER = 21

def CreateRandomNumber():
    rnd = random.randrange(CONST_LOW_NUMBER, CONST_HIGH_NUMBER)
    return rnd

def GuessTheNumber():
    print("Welcome to GuessTheNumber!")
    
    userGuess = input("Please choose a number between %s & %s:   " % (CONST_LOW_NUMBER, CONST_HIGH_NUMBER - 1))
    CheckUserGuess(userGuess, CreateRandomNumber())
    
def CheckUserGuess(guess, randomNumber):
    try:
        value = int(guess)             
    except ValueError:
        newValue = input("Your answer is not a number.  \nPlease guess again:   ")
        CheckUserGuess(newValue, randomNumber)
    else:
        value = int(guess)
        if (value < CONST_LOW_NUMBER) or (value > CONST_HIGH_NUMBER - 1):
           newValue = input("Your answer is outside the range of numbers.  \nPlease choose again:   ")
           CheckUserGuess(newValue, randomNumber)
        elif (value > randomNumber):
           newValue = input("Your answer is too %s.  \nPlease choose again:   " % ("high"))
           CheckUserGuess(newValue, randomNumber)
        elif (value < randomNumber):
            newValue = input("Your answer is too %s.  \n Please choose again:   " % ("low"))
            CheckUserGuess(newValue, randomNumber)
        else:
            print("Your answer is correct!  The number was %s!" % randomNumber) 
    
GuessTheNumber()