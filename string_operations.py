# a list of programming languages
my_list=['Python', 'C++', 'JavaScript', 22, 33]
lenlength=len(my_list)
## len will not work if 
## negative indexing
#print(my_list[-1]) #3 -1 and 2(number of items are same)

##iterate each item
for item in my_list:
    item_val = str(item)
    length = len(item_val)
    print(f"\nThe length of '{item}' is {length}")
    #print(item[:length]) # to print whole item values
    ## iterating indvidual list items
    for i in range(length):        
        #print(item[i][:],end='') ## print in one lines
        #print(item[i][:]) ## print in seperate lines cahercter by charecter same print(item[i])
        #print(item[i],end="") #3 end introduces comma, special charectror at the end. If none passed all charectors line by line
        #print(*item[i]) #3 * for unpacking
        if type(item) == str:
            print(item[i],end='') #3 * for unpacking
        else:
            print(item)
        
        

