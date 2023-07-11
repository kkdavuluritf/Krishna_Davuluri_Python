import itertools
#x = [1, 2, 3,4,5,6,7,8,9,10]
x = [10,11,12,13,15,18]
y = ['a', 'b', 'c']

def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    print('Num Group',num_groups)
    print('Length', len(inputs))
## print(tuple(inputs[i*n:(i+1)*n])
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

list1 = naive_grouper(x, 3)
print(list1)