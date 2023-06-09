if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr1 = sorted(arr, key=lambda x : x[k], reverse = False)
    for i in arr1:
        print(*i)

# Input Format
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.
# Output Format
# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
# Sample Input 0
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# Sample Output 0
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
# Explanation 0
# The details are sorted based on the second attribute, since K is zero-indexed.
