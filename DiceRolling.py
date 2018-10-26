import random


def rolldie():
    die = random.randint(1,6)
    return die

die1 = 1
die2 = 1

print('Welcome to the dice rolling program')
user_input = input('Enter 1 to roll one dice and 2 to roll two die and q to quit:')

while (user_input != 'q'):
    if (user_input == '1'):
        print('Your rolled a:', rolldie())
    elif(user_input == '2'):
        print('You rolled a', rolldie(), 'and a', rolldie())
    elif(user_input == 'q'):
        print ('Program ended')
    else:
        print ('Error, wrong value entered')

    user_input = input('Enter 1 to roll one dice and 2 to roll two die and q to quit:')


