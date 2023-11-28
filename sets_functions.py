##
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

def cartesian_product(A, B):
##calculates the Cartesian product of two sets A and B
    return {(a, b) for a in A for b in B}

#print('Set unions:', set_a|set_b)
print('Set unions:', set_a.union(set_b))
#print('Set intersections:', set_a&set_b)
print('Set intersections:', set_a.intersection(set_b))

print('A Set Difference:', set_a-set_b)
print('B Set Difference:', set_b-set_a)

print('Set Symmetric Difference:', (set_a.union(set_b))-(set_a.intersection(set_b)))
##Symmetric Difference of A and B is a set of elements in A and B but not in both (excluding the intersection).
##Symmetric difference is performed using ^ operator. Same can be accomplished using the method
## To figure out different items in two sets
##print('Symmetric difference:', set_a ^ set_b)
print('cartesian_product:' ,cartesian_product(set_a,set_b))

set_a.add(10)  ## ADD takes one argument
set_c = set_a.copy()
print('Copied set from A:', set_c)
#set_b.add((10,20,30)) ## ADD list as one argument IS NOT possible. Tuple is possibe
#print('Added list to Set B:', set_b)

def difference_update(A, B):
###"""Removes all elements of second parameter from first parameter:: Updates first parameter ."""
    A.difference_update(B)
"""
difference_update(set_b, set_a)
print('Difference update:', set_a)
"""
def intersection_update(A, B):
## Updates Parameter1 to contain only the elements that are also in Parameter2."""
  A.intersection_update(B)
"""
intersection_update(set_b, set_a)
print('Intersection Update:', set_a)
"""
total_a = sum(list(set_a))
total_b = sum(list(set_b))
print(total_a)
print(f'Sum of {set_a} and {set_b} is {total_a} and {total_b}')

set_a.add(30)
len = len(set_a)
print('added item:', set_a)
"""
len = int(len-1)
set_a.remove(len)  "" len is not working, index works
print('Removed item:', set_a)
"""

set_a.pop()  ##Pop from index 0
print('Popped item:', set_a)
