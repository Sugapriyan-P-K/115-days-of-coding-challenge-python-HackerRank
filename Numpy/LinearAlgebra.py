import numpy
n = int(input())
arr = numpy.array([input().strip().split() for i in range(n)], float)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(arr))

# Task
# You are given a square matrix A with dimensions N X N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.
# Sample Input
# 2
# 1.1 1.1
# 1.1 1.1
# Sample Output
# 0.0
