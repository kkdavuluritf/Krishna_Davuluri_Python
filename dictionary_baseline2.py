# get vs [] for retrieving elements
my_dict = {'name': ['Jack','Mike','Angila','Robin'], 'age': [27,29,26,27]}
list_age = my_dict['age']
list_name = my_dict['name']
i = 0
for item in list_age:
    if item >= 27:
        print('Name and Age:', list_name[i], item)
    i = i+1




