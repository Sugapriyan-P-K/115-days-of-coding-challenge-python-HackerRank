import numpy
a,b = map(int, input().split())
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(a,b,k=0))
#print(numpy.identity(a,b))

# Task
# Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.
# Sample Input
# 3 3
# Sample Output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
