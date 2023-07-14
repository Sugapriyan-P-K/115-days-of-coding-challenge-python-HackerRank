cube = lambda x: x*x*x # complete the lambda function 
def fibonacci(n):
    n1,n2 = 0,1
    l = [0,1]
    if n==0:
        return []
    elif n==1:
        return [n1]
    else:
        for i in range(2,n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            l.append(n2)
        return l
    # return a list of fibonacci numbers
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# Sample Input
# 5
# Sample Output
# [0, 1, 1, 8, 27]
# Explanation
# The first 5 fibonacci numbers are [0,1,1,2,3], and their cubes are [0,1,1,8,27].
