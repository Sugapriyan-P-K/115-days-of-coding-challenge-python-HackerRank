import numpy
numpy.set_printoptions(sign=' ')
arr = numpy.array(input().split(), float)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

# Task
# You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.
# Sample Input
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
# Sample Output
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
