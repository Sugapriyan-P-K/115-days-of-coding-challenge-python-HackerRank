import numpy
n,m,p = map(int, input().split())
arr1 = numpy.array([input().strip().split() for _ in range(n+m)], int)
print(arr1)

# Task
# You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
# Sample Input
# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4 
# Sample Output
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]] 
