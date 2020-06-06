#for target_list in expression_list:
import random, sys

for i in range(5): # = for i in range(0, 5, 1) = for(int i = 0; i < 5; i++)
    print('i = ' + str(i))
    print('random number= ' + str(random.randint(0, 5))) #prints a random integer on [0-5] interval

while True:
    print('Make a guess between 0 and 5:')

    rand = random.randint(0, 5)
    if int(input()) == rand:
        print('The number was: ' + str(rand) + ' CONGRATS!!!')
        sys.exit();
    else: print('The number was: ' + str(rand) + ' try again!')
