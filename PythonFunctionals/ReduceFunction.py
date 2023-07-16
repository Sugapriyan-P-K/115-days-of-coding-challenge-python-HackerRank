from fractions import Fraction
from functools import reduce
def product(fracs):
    t = reduce(lambda x, y : x * y,  fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

# Sample Input 0
# 3
# 1 2
# 3 4
# 10 6
# Sample Output 0
# 5 8
# Explanation 0
# Required product is (1/2)*(3/4)*(10/6) = 5/8
