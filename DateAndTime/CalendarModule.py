from datetime import datetime
date = input()
date = datetime.strptime(date, "%m %d %Y")
print(date.strftime("%A").upper())

# Task
# You are given a date. Your task is to find what the day is on that date.
# Sample Input
# 08 05 2015
# Sample Output
# WEDNESDAY
# Explanation
# The day on August 5th 2015 was WEDNESDAY.
