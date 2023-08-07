regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"
import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# A valid postal code  have to fullfil both below requirements:
# 1. P must be a number in the range from 100000 to 999999 inclusive.
# 2. P must not contain more than one alternating repetitive digit pair.
# Alternating repetitive digits are digits which repeat immediately after the next digit. 
# In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
# For example:
# 121426 # Here, 1 is an alternating repetitive digit.
# 523563 # Here, NO digit is an alternating repetitive digit.
# 552523 # Here, both 2 and 5 are alternating repetitive digits.
# Sample Input 0
# 110000
# Sample Output 0
# False
# Explanation 0
# 1 1 0000 : (0, 0) and (0, 0) are two alternating digit pairs. Hence, it is an invalid postal code.
# Note:
# A score of 0 will be awarded for using 'if' conditions in your code.
# You have to pass all the testcases to get a positive score.
