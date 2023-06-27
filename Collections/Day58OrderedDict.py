from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    *s,n = input().rsplit()
    s = " ".join(j for j in s if j.isalpha())
    n=int(n)
    if s in d.keys():
        v=d.get(s)
        n=v+n
    d[s]=n
for key,value in d.items():
   print(key,value)

# Sample Input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
# Sample Output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20
# Explanation
# BANANA FRIES: Quantity bought: 1, Price:12 
# Net Price: 12
# POTATO CHIPS: Quantity bought: 2, Price: 30
# Net Price: 60
# APPLE JUICE: Quantity bought: 2, Price: 10
# Net Price: 20
# CANDY: Quantity bought: 4, Price: 5
# Net Price:20
