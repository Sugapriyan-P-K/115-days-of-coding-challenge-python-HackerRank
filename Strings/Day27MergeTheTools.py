def merge_the_tools(string, k):
    for i in range(0, len(string),k):
        s=string[i:i+k]
        print(''.join(sorted(set(s),key=s.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Example
# s = 'AAABCADDE'
# k=3
# There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1='A'. The second substring has all distinct characters, so u2='BCA'. 
# The third substring has 2 different characters, so u3 = 'DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

# Function Description
# merge_the_tools has the following parameters:
#   string s: the string to analyze
#   int k: the size of substrings to analyze
# Prints
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.

# Input Format
# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.
