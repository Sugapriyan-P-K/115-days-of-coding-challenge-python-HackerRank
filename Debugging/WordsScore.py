

# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
# Consider that vowels in the alphabet are a, e, i, o, u and y.
# Function score_words takes a list of lowercase words as an argument and returns a score as follows:
# The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1. 
# The score for the whole list of words is the sum of scores of all words in the list.
# Debug the given function score_words such that it returns a correct score.
# Your function will be tested on several cases by the locked template code.
# Sample Input 1
# 3
# programming is awesome
# Sample Output 1
# 4
# Explanation 1
# There are 3 words in the input: programming, is and awesome. The score of programming is 1 since it contains 3 vowels, an odd number of vowels. 
# The score of is is also 1 because it has an odd number of vowels. The score of awesome is 2 since it contains 4 vowels, an even number of vowels. 
# Thus, the total score is 1 + 1 + 2 = 4.
