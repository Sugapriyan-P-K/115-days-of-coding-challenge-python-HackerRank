from itertools import combinations
n = int(input())
l = (list(map(str, input().split())))
k = int(input())
p = combinations(l, k)
ct,cp= 0,0
for i in p:
    ct += 1
    if 'a' in i:
        cp += 1
print(f'{cp/ct:.4f}')

# Sample Input
# 4 
# a a c d
# 2
# Sample Output
# 0.8333
# Explanation
# All possible unordered tuples of length  comprising of indices from 1 to 4 are:
# (1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
# Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.
# Hence, the answer is 5/6 => 0.8333.
