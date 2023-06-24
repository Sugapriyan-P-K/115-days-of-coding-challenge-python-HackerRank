# without Counter
# n = int(input())
# x = map(int, input().split())
# x = list(x)
# c = 0
# for i in range(int(input())):
#     s, p = map(int, input().split())
#     if s in x:
#         x.remove(s)
#         c = c + p
# print(c)  
# with Counter
from collections import Counter
n_shoes = int(input())
shoes = input().split()
size = Counter(shoes)
n = int(input())
money = 0
for i in range(n):
    s, p = input().split()
    if size[s] > 0:
        size[s] -= 1
        money += int(p)
print(money)

# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
# Sample Input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output
# 200
# Explanation
# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.
# Total money earned 55 + 45 + 40 + 60 =  $200.
