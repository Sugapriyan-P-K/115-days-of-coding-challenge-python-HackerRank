# on pypy3
import re
for i in range(int(input())):
    try:
        re.compile(input())
        print('True')
    except Exception as e:
        print('False')

# You are given a string S.
# Your task is to find out whether S is a valid regex or not.
# Sample Input
# 2
# .*\+
# .*+
# Sample Output
# True
# False
# Explanation
# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.
