import cmath
def square2(input_num):
#        inputs_num = input_num ** 2
    return [input_num**2]
# no formal and actual parameters
# value you sent can be changed and bough back"
number = int(input("Please enter list of numbers to find squares :"))
squares = square2(number)
print(f'Sqaure to the number{number} is {squares}')

# calculated squares are in list1. Actual input to list1 is changed
