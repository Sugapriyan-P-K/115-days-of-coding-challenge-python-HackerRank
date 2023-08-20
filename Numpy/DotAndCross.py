import numpy
n = int(input())
arr1 = numpy.array([input().strip().split() for _ in range(n)], int)
arr2 = numpy.array([input().strip().split() for _ in range(n)], int)
print(numpy.dot(arr1,arr2))

# Task
# You are given two arrays A and B. Both have dimensions of N X N.
# Your task is to compute their matrix product.
# Sample Input
# 2
# 1 2
# 3 4
# 1 2
# 3 4
# Sample Output
# [[ 7 10]
#  [15 22]]
