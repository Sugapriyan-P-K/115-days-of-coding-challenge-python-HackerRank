import numpy
a1 = numpy.array(input().strip().split(), int)
a2 = numpy.array(input().strip().split(), int)
print(numpy.inner(a1,a2), numpy.outer(a1,a2), sep='\n')

# Task
# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.
# Sample Input
# 0 1
# 2 3
# Sample Output
# 3
# [[0 0]
# [2 3]]
