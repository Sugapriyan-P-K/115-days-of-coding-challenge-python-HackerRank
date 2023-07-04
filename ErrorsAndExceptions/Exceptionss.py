for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print('Error Code:', e)

# Task
# You are given two values a and b.
# Perform integer division and print a/b.
# Sample Input
# 3
# 1 0
# 2 $
# 3 1
# Sample Output
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3
# Note:
# For integer division in Python 3 use //.
