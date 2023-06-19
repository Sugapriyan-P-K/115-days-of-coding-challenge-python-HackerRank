from itertools import combinations
s,k = input().split()
s = sorted(list(s))
for i in range(1,int(k)+1):
    S = list(combinations(s,i))
    print(*("".join(j) for j in S),sep="\n")

# Task
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
# Sample Input
# HACK 2
# Sample Output
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
