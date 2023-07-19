

# You are given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:
# +91 xxxxx xxxxx
# The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.
# Sample Input
# 3
# 07895462130
# 919875641230
# 9195969878
# Sample Output
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230
# Concept
# To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. 
# Make a decorator that standardizes the mobile numbers and apply it to the function.
