for i in range(int(input())):
    x, a , y, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))

# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.
# Sample Input
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# Sample Output
# True 
# False
# False
# Explanation
# Set A = {1 2 3 5 6}
# Set B = {9 8 5 6 3 2 1 4 7}
# All the elements of set A are elements of set B.
# Hence, set A is a subset of set B.
