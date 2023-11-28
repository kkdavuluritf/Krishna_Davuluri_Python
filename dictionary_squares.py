# get vs [] for retrieving elements
my_dict = {'number': [1,2,3,4,5], 'square': [10,10,10,20,20,10,989,99089]}
print('Before changes:', my_dict)
list_number = my_dict['number']
list_square = my_dict['square']
i = 0
"""for k,v in my_dict.items():
    if k=='number':
#        my_dict['square']=4
        print('key is 2')
        """

for items in list_number:
    list_square[i]=items**2
    i=i+1

print('After changes:', my_dict)