from itertools import product, permutations

"""
Generate Cartesian product
'*' unpack prd list into separate arguments
output: [('a', '1'), ('a', '2'), ('a', 'c'), ('b', '1'), ('b', '2'), ('b', 'c')]
list(iterator) because need to printout, if without list() will be obj
"""
prd = [['a', 'b'], ['1', '2', 'c']]
print(list(product(*prd)))
#same as below
prd1 = ['a', 'b']
prd2 = ['1', '2', 'c']
prd3 = ['3']
print(list(product(prd1, prd2, prd3)))

data = ['a','b','c']
# permutation of length 2
res = list(permutations(data, 2))
print(res)