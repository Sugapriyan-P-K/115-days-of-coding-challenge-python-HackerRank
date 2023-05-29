n,m  = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int,input().split()))
happiness = 0
for i in range(n):
    if arr[i] in A:
        happiness+=1
    elif arr[i] in B:
        happiness-=1
print(happiness)


# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B.
# Your initial happiness is 0. For each i integer in the array, if i ∈ A, you add 1 to your happiness. If i ∈ B, you add -1 to your happiness. Otherwise, your happiness does not change.
# Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
  
# Sample Input
# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output
# 1
