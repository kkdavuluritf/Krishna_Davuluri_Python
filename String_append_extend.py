#Appending and Extending lists in Python
odd = [1, 3, 5]
print(f'new list',odd)
odd.append(7)

print(f'Append',odd)  #[1,3,5,7]  # single item use append

odd.insert(1,int(10))

print(f'Insert:',odd)  #[1,3,5,7,9,11,13]

odd.extend([9, 11, 13,15])  # multiple items use extend
print(f'Extend:',odd)
# remove
odd.remove(odd[2])
print(f'Remove:',odd)
# count
print(f'Count:', odd.count(1))
# Sort
odd.sort()
print(f'Sort:', odd)

# clear
#odd.clear()
#print(f'Clear:',odd)
length = len(odd)
# 2 powers
pow2 = [2**i for i in range(10)]
print('Power', pow2)

# copy
new_odd=odd.copy()
print('New copied odd:', new_odd)
#3 new odd squares
new_oddsquare=[]
for item in odd:
    new_oddsquare.append(item**2)

print('Squares', new_oddsquare)
