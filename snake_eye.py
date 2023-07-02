import  random

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
count = 1

while roll1 != 1 or roll2 != 1:
    #print('Roll1', roll1, 'Roll2', roll2)
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    count += 1

print('Roll1:', roll1, 'Roll2:', roll2, 'in ', count , ' times')