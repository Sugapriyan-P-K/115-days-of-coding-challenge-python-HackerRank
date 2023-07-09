n,m= map(int,input().split())
print(eval(input().replace('x',str(n)))==m)

# Task
# You are given a polynomial P of a single indeterminate (or variable), x.
# You are also given the values of x and k. Your task is to verify if P(x) = k.
# Sample Input
# 1 4
# x**3 + x**2 + x + 1
# Sample Output
# True
# Explanation
# P(1) = 1**3 + 1**2 + 1 + 1 = 4 = k (where k = 4)
# Hence, the output is True.
