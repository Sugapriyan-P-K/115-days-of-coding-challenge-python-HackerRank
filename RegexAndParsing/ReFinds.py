import re
c = 'qwrtypsdfghjklzxcvbnm'
v = 'aeiou'
l=(re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (c, v, c),input(), flags =re.I))
print(*l, sep='\n') if len(l)>0 else print('-1')

# Task
# You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.
# Note :
# Vowels are defined as: AEIOU and aeiou.
# Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.
# Sample Input
# rabcdeefgyYhFjkIoomnpOeorteeeeet
# Sample Output
# ee
# Ioo
# Oeo
# eeeee
# Explanation
# ee is located between consonant d and f.
# Ioo is located between consonant k and m.
# Oeo is located between consonant p and r.
# eeeee is located between consonant t and t.
