import math
AB, BC= int(input()),int(input())
hypo = math.hypot(AB,BC)
angle_mbc = str(round(math.degrees(math.acos(BC/hypo))))
degree_symbol = chr(176)
print(angle_mbc+degree_symbol)


# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.
# Sample Input
# 10
# 10
# Sample Output
# 45°
