from itertools import permutations 
s,k = input().split()
k = int(k)
per_str = sorted(list(permutations(s,k)))
for i in per_str:
    print("".join(list(i)))

# Task
# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
# Sample Input
# HACK 2
# Sample Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# Explanation
# All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.
