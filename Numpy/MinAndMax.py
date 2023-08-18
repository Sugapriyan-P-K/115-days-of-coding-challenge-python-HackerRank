import numpy
n,m = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(n)], int)
a_min = numpy.min(arr, axis=1)
print(max(a_min))

# Task
# You are given a 2-D array with dimensions N X M.
# Your task is to perform the min function over axis 1 and then find the max of that.
# Sample Input
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0
# Sample Output
# 3
# Explanation
# The min along axis 1 = [2,3,1,0]
# The max of [2,3,1,0] = 3
