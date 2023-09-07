import random

counter = 0
for num in range(1,102,1):
    rem = num % 2
    if  ( rem == 0 ):
        print('Even:', num)
    else:
        print('Odd:', num)
    counter += 1
    #06/28/2023