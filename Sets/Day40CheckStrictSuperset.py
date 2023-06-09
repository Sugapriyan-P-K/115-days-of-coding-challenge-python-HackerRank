s = set(map(int, input().split()))
n = int(input())
dic = {}
for i in range(n):
    s2 = set(map(int, input().split()))
    var = s.issuperset(s2)
    dic.setdefault(i,var)
if all(dic.values())==True:
    print("True")
else:
    print("False")



# Sample Input 0
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Sample Output 0
# False
# Explanation 0
# Set A is the strict superset of the set ([1,2,3,4,5]) but not of the set ([100,11,12]) because 100 is not in set A.
# Hence, the output is False.
