import cmath
def square2(inputs):
    len1 = len(inputs)
##for loop
    for i in range(0,len1,1):
        inputs1 = inputs
        inputs[i]= inputs[i] ** 2
    return [inputs1]
# no formal and actual parameters
# value you sent can be changed and bough back"
number_list = []
counter = 1
while True:
    number = int(input("Please enter list of numbers to find squares 0 to exit:"))
#    number_list.insert(number, counter)
    if number == 0:
        break
    number_list.append(number)
    counter = counter + 1

#list1 = [1,2,3,4,5,6,7]
list1 = []
list1 = number_list
print('numbers before call are:', number_list)
squares = square2(number_list)
print('numbers after call are:', number_list)
# calculated squares are in list1. Actual input to list1 is changed
print('List1 after call are:', list1)

# length calculation
len1 = len(list1)
## square root prints

for i in range(0,len1,1):
    print(f'number: {number_list[i]}, square: {list1[i]}')
