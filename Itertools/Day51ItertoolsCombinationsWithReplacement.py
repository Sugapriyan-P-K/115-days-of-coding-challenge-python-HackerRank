from itertools import combinations_with_replacement
s,k = input().split()
l = list(combinations_with_replacement(sorted(s), int(k)))
for i in l:
    print("".join(list(i)))

# Task
# You are given a string S.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
# Sample Input
# HACK 2
# Sample Output
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK
