import math
prime_list = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,87,89,91,93,97]
for number in range(1,101):
    if number not in prime_list:
        print(number)
    else:
        print("Prime")