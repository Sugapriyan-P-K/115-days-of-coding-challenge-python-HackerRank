import numpy
ar = map(int, input().split())
arr = list(ar)
a1 = numpy.array([arr], int)
print(a1.reshape(3,3))

# Task
# You are given a space separated list of nine integers. Your task is to convert this list into a 3 X 3 NumPy array.
# Sample Input
# 1 2 3 4 5 6 7 8 9
# Sample Output
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
