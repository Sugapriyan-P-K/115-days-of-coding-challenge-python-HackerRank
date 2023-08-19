import numpy
n,m = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(n)], int)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
out = numpy.std(arr, axis=None)
if  out==0:
    print("{0:.1f}".format(out))
else:
    print("{0:.11f}".format(out))

# Task
# You are given a 2-D array of size N X M.
# Your task is to find:
# The mean along axis 1
# The var along axis 0
# The std along axis None
# Sample Input
# 2 2
# 1 2
# 3 4
# Sample Output
# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875
