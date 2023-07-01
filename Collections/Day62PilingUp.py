def pilingUpCubes(cubeList):
    if max(cubeList)==cubeList[len(cubeList)-1] or max(cubeList)==cubeList[0]:
        return True
    else:
        return False
    
def parseTestcase():
    numberOfBlocks = int(input())
    return [int(x) for x in input().split()]

if __name__ == '__main__':
    for testcase in range(int(input())):
        resultOfTestcase = pilingUpCubes(parseTestcase())
        print('Yes' if resultOfTestcase else 'No')

# There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: 
# if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].
# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.
# Sample Input
# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]
# Sample Output
# Yes
# No
# Explanation
# In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
# In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.
