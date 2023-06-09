from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
car_product = product(A,B)
for i in car_product:
    print(i,end=" ")

# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
# Task
# You are given a two lists A and B. Your task is to compute their cartesian product A X B.
# Sample Input
#  1 2
#  3 4
# Sample Output
#  (1, 3) (1, 4) (2, 3) (2, 4)
