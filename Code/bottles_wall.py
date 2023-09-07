import random
for number_bottles in range(100,0,-1):

    if number_bottles - 1 != 0:
        print(f'{number_bottles} bottles of beer on the wall.')
        #print(f'{number_bottles} bottles of beer.')
        print(f'take one down,pass it around, {number_bottles-1} bottles of beer on the wall.')
    else:
        print(f'{number_bottles} bottle of beer on the wall.')
        #print(f'{number_bottles} bottle of beer.')
        print(f'take one down,pass it around and no more bottles of beer on the wall.')
    print('*'*70)