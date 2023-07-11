import random
text_letter = 'I am Krishna Davuluri. Trying to test the for loop'
counter = 0
for letter in text_letter:
    rem = counter % 5
    if  ( rem == 0 ):
        print('\t', letter)
    else:
        print(letter)
    counter += 1