import random
first_name = input("Enter First name:")
last_name = input("Enter Last name:")
string_len = len(first_name) + len(last_name)
print('*' * 100)
if string_len < 15:
    print("Length is less than 15")

elif string_len > 22:
    print("Length is less than 22 and greater than 15")
else:
    print("Length is greater than 22")

print('*'*100)
#ran_num = random.randint(0,1)

#if  ran_num == 30:
#    print("Heads")
#else:
#    print("Tails")