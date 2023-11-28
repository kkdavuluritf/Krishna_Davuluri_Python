new_list=[10,33,43,2,6,3,89,343,-4]

new_list.sort()
print("Sorted:", new_list)

#new_list_copy = new_list Direct assignment
new_list_copy=new_list.copy()
print("Copied list:",new_list_copy)

new_list_copy.extend([10,767,87867])
#print("Copied list extended:",new_list_copy)
new_list_copy.insert(5,'Hello world')

#print("Copied list extended copy:",new_list_copy)

new_list_copy[4]= 'November'
print("Copied list extended copy:",new_list_copy)

new_list_copy.remove(89)
print("Copied list deleted:",new_list_copy)

new_list_copy.append(100)
print("Copied list extended:",new_list_copy)
new_even_list=[]
for item in new_list:    
    if item % 2==0:
        new_even_list.append(item**2)
print('Square of even', new_even_list)

new_list_squares = [2**item for item in new_list]
print("Squares are:",new_list_squares)



new_list.extend([56,98,-10])     
new_list.sort()
print("Sorted:", new_list)

