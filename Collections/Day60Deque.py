from collections import deque
d=deque()
for i in range(int(input())):
    arg=input().split()
    if arg[0]=="append":
        d.append(arg[1])
    elif arg[0]=="appendleft":
        d.appendleft(arg[1])
    elif arg[0]=="popleft":
        d.popleft()
    else:
        d.pop()
print(*d)

# Task
# Perform append, pop, popleft and appendleft methods on an empty deque d.
# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
# Sample Output
# 1 2
