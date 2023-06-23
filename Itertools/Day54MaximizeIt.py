

# You are given a function f(x) = X^2. You are also given K lists. The iTH list consists of Ni elements.
# You have to pick one element from each list so that the value from the equation below is maximized:
# S = (f(X1) + f(X2) + ... + f(Xk))%M
# Xi denotes the element picked from the iTH list . Find the maximized value Smax obtained.
# % denotes the modulo operator.
# Note that you need to take exactly one element from each list, not necessarily the largest element. 
# You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
# Sample Input
# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 
# Sample Output
# 206
# Explanation
# Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum S value equal to (5^2 + 9^2 + 10^2) % 1000 = 206.
