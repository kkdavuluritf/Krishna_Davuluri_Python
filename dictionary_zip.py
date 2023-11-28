#3my_dict = {'Name':['Nithya', 'Smaira'], 'Age':[8,9]}
#list_keys = ['Name','Age']
#list_values=[['Nithya', 'Samira'], [8,9]]
#list_keys = ['Nithya','Samaira']
#list_values=[8,9]

"""
my_dict ={list_keys:list_values for list_keys,
		  list_values in zip(list_keys, list_values)}

j=0
#for i, (name, age) in enumerate(zip(my_dict.keys(), my_dict.values())):
for i, (name, age) in enumerate(zip(list_keys, list_values)):
#print(j,my_dict['Name',list],my_dict['Age'])    
    print(list_values[0][1] )
    j=j+1
"""
new_dict={}


"""
stocks = ['GEEKS', 'For', 'geeks','New']
prices = [2175, 1127, 2750,400]

new_dict = {stocks: prices for stocks,
			prices in zip(stocks, prices)}
print(new_dict)"""
"""

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]

# using zip() to map values
mapped ={zip(name, roll_no)}

print(mapped)"""
## Enumerate
"""
names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]
Marks = [60,70,80]
j = 1
for i, (name, age, marks) in enumerate(zip(names, ages,Marks)):
	print(j,'\t',name,'\t',age,'\t',marks)
	j=j+1"""
	