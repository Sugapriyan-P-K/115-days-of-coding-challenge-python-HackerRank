import numpy
n,m = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(n)], int)
print(arr.transpose())
print(arr.flatten())

# Task
# You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.
# Sample Input
# 2 2
# 1 2
# 3 4
# Sample Output
# [[1 3]
#  [2 4]]
# [1 2 3 4]
