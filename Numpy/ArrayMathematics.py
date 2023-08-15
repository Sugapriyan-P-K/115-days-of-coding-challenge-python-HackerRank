import numpy
n,m = map(int,input().split())
arr1 = numpy.array([input().strip().split() for _ in range(n)], int)
arr2 = numpy.array([input().strip().split() for _ in range(n)], int)
print(numpy.add(arr1,arr2))
print(numpy.subtract(arr1,arr2))
print(numpy.multiply(arr1,arr2))
a = numpy.array(numpy.divide(arr1,arr2), int)
print(a)
b = numpy.array(numpy.mod(arr1,arr2), int)
print(b)
print(numpy.power(arr1,arr2))

# Task
# You are given two integer arrays, A and B of dimensions N X M.
# Your task is to perform the following operations:
# Add (A + B)
# Subtract (A - B)
# Multiply (A * B)
# Integer Division (A / B)
# Mod (A % B)
# Power (A ** B)
# Sample Input
# 1 4
# 1 2 3 4
# 5 6 7 8
# Sample Output
# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]] 
