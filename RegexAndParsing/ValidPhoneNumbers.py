import re
for i in range(int(input())):
    if bool(re.search(r'^[7-9](\d{9})$', input())):
        print('YES')
    else:
        print('NO')

# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.
# Sample Input
# 2
# 9587456281
# 1252478965
# Sample Output
# YES
# NO
