n = int(input())
a = set(map(int, input().split()))
n2 = int(input())
b = set(map(int, input().split()))
s = a.union(b)
print(len(s))


# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output
# 13
# Explanation
# Roll numbers of students who have at least one subscription:
# 1,2,3,4,5,6,7,8,9,10,11,21 and 55. Roll numbers: 1,2,3,6 and 8 are in both sets so they are only counted once.
# Hence, the total is  students.
