import cmath
def square2(inputs):
    len1 = len(inputs)
##for loop
    for i in range(0,len1,1):
        #inputs1 = inputs
        inputs[i]= inputs[i] ** 2
    return [inputs]
# no formal and actual parameters
# value you sent can be changed and bough back"
# list 1
number_list1 = []
number_list2 = []
counter = 1
while True:
    number = int(input("Please enter list1 of numbers to find squares 0 to exit:"))
#    number_list.insert(number, counter)
    if number == 0:
        break
    number_list1.append(number)
    counter = counter + 1
### list 2
counter = 1
while True:
    number = int(input("Please enter list2 of numbers to find squares 0 to exit:"))
#    number_list.insert(number, counter)
    if number == 0:
        break
    number_list2.append(number)
    counter = counter + 1

# append the numbers
number_list3 = number_list1+number_list2
print(number_list3)