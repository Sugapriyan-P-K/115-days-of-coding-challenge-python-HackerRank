import cmath
z = complex(input())
x = z.real
y = z.imag
r = cmath.sqrt(pow(x,2)+pow(y,2))
print(r.real)
print(cmath.phase(z))

# Task
# You are given a complex z. Your task is to convert it to polar coordinates.
# Sample Input
#   1+2j
# Sample Output
#  2.23606797749979 
#  1.1071487177940904
# Note: The output should be correct up to 3 decimal places.
