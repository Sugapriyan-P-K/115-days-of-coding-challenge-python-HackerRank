orderToSort = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key = orderToSort.index),sep='')

# You are given a string S.
# S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Sample Input
# Sorting1234
# Sample Output
# ginortS1324
