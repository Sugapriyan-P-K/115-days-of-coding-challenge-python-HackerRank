from collections import Counter 
d = Counter([input() for i in range(int(input()))])
print(len(d))
print(*d.values())

# You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.
# See the sample input/output for clarification.
# Note: Each input line ends with a "\n" character.
# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output
# 3
# 2 1 1
# Explanation
# There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. 
# The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
