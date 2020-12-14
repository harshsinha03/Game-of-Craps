

# players are given a option to start the game or to quit by importing sys module.

import sys
a=input("TO START THE GAME TYPE 'yes' and TO QUIT TYPE 'no'\n")
if a.lower()=="no":
    sys.exit()
else:
    print("LET'S START THE GAME")
# those who need instructions can ask for it, others can start the game directly.

a=input("welcome to the game of chance,are you ready to test your fortune ,\ndo you need instructions type (yes) or (no) \n")
if a.lower()=="yes":
    print(''' 1. player rolls two six-sided dice and adds the numbers rolled together.
              2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12automatically loses, and play is over.
                 If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the 'point.'
              3. The player continues to roll the two dice again until one of two things happens: 
                 either they roll the 'point' again, in which case they win; or they roll a 7, in which case they lose.''')
elif a.lower()=="no":
    print("all the best, player")




import random      # for random number generation.

def dice_number():
    _=input("press enter to roll the dice ") #using "_ " because python ignores a variable if "_" is used. This is an unused variable but important so that we can have the press enter option.
    die1 = random.randrange(1,7)  # this will enable to select a random number from 1 to 6
    die2 = random.randrange(1,7) 
    return (die1 , die2)          #returns the dice_number values in the form of tuple

   
def two_dice(dices):
    die1, die2 = dices
    print("player- the sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(die1,die2,sum(dices)))# using string formatting to input the values of die1 and die2 and then using the sum function for die1+die2  # as previously the return value returned die1 and die2 in tuple, this will convert them into variables.

value=dice_number() #calling the dice_number function to get a value,return the roll and then store that value in value.
two_dice(value) 
sum_of_dices=sum(value) #using the sum function in value to find the sum of two outcomes.

#sample executions

if sum_of_dices in (7,11): # why we are using (in) keyword to find if sum of dices is 7 or 11 to determine the result.
    result="congratulations you won"
elif sum_of_dices in (2,3,12): #  we are using (in) keyword to find if sum of dices is 2 , 3 , 12 to determine the result.
    result="you lost, \ntry again next time"
else: #because none of the cases worked above now we will play continously until we win or lose.
    result="continue your game please"
    currentpoint = sum_of_dices
    print("good game, your current point is",currentpoint)


# game continues if you have not scored a total of 2 , 3 , 7 , 11 , 12 
while result=="continue your game please":# this will enable the game to continue in a loop until the outcome is win or lose
    value=dice_number()
    two_dice(value)
    sum_of_dices=sum(value)
    if sum_of_dices == currentpoint:
        result="congratulations you won"
    elif sum_of_dices == 7:
        result="you lost,\n try again next time"

# when the outcome is clear,this will produce the outcome of the game
if result == "congratulations you won":
    print("congratulations,you won")
else:
    print("you lost, \ntry again next time")



