n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    a = (input().strip().split())
    if a[0]=="pop":
        s.pop()
    if a[0]=="remove":
        s.remove(int(a[1]))
    if a[0]=="discard":
        s.discard(int(a[1]))
print(sum(s))


# Task
# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5
# Sample Output
# 4
# Explanation
# After completing these 10 operations on the set, we get set ([4]). Hence, the sum is 4.
# Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to 
# the editor.
