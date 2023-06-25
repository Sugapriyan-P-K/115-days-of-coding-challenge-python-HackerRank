from collections import defaultdict
n,m = map(int,input().split())
A=defaultdict(list)
for i in range(n):
    A[input()].append(i+1)
B=[input() for i in range(m)]
for i in B:
    if i in A:
        print(" ".join(map(str,A[i])))
    else:
        print('-1')

# Sample Input
# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b
# Sample Output
# 1 2 4
# 3 5
# Explanation
# 'a' appeared 3 times in positions 1, 2 and 4.
# 'b' appeared 2 times in positions 3 and 5.
# In the sample problem, if 'c' also appeared in word group B, you would print -1.
