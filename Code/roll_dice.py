import random
import itertools
#rolls = int(input("Number of rolls:"))
#sides = int(input("Number of sides:"))
## check i = 0 and exit
counter = 1
int_count = int(0)
for i in itertools.count():
    if counter > 1:
        i = int(input('Roll again? (Enter 0 to Quit)'))
    else:
        i = 1
    if i == 0:
        break
    else:
        rolls = int(input("Number of rolls:"))
        sides = int(input("Number of sides:"))
    result = ' '
    int_count = int(0)
    for die in range(rolls):
        int_count = int(int_count+1)
        rand = random.randint(1,sides)
        result = f'\tRoll count{int_count}   value of the roll {rand}|'
        #print('Inner',random.randint(1,sides))
        print('Result:',result)
    counter+= counter