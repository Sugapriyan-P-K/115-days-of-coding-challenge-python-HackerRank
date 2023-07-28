import re
for i in range(int(input())):
    s = re.sub(r' &&(?= )', ' and', input())
    print(re.sub(r' \|\|(?= )', ' or', s))

# Task
# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
# && → and
# || → or
# Both && and || should have a space " " on both sides.
# Sample Input
# 11
# a = 1;
# b = input();

# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b)) 
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.
# Sample Output
# a = 1;
# b = input();

# if a + b > 0 and a - b < 0:
#     start()
# elif a*b > 10 or a/b < 1:
#     stop()
# print set(list(a)) | set(list(b)) 
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.    
