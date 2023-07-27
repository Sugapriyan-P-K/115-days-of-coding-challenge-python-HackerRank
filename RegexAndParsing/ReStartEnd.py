import re
s = input()
k = input()
M = re.finditer(r'(?=('+k+'))', s[:len(s)],0)
m = [(m.start(1), m.end(1)-1) for m in M]
if len(m)>0:
    print(*m, sep='\n')
else:
    print('(-1, -1)')


# Task
# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.
# Sample Input
# aaadaa
# aa
# Sample Output
# (0, 1)  
# (1, 2)
# (4, 5)
