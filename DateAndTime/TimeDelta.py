import math
from datetime import datetime


def time_delta(t1, t2):
    format_date = "%a %d %b %Y %H:%M:%S %z"
    return str(int(abs((datetime.strptime(t1, format_date)-datetime.strptime(t2, format_date)).total_seconds())))

# Sample Input 0
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0
# 25200
# 88200
# Explanation 0
# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7*3600 seconds or 25200 seconds.
# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 
# 24 * 3600 + 30 * 60 = 88200
