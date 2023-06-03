n = int(input())
s = set(input().split())
n1 = int(input())
s1 = set(input().split())
print(len(s.intersection(s1)))


# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output
# 5
# Explanation
# The roll numbers of students who have both subscriptions:
# 1,2,3,6 and 8.
# Hence, the total is 5 students.
