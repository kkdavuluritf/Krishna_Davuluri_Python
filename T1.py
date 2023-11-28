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

print('cartesian_product:' ,cartesian_product(set_a,set_b))

set_a.add(10)  ## ADD takes one argument
set_c = set_a.copy()
print('Copied set from A:', set_c)
set_b.add((10,20,30)) ## ADD list as one argument IS NOT possible. Tuple is possibe
print('Added list to Set B:', set_b)
