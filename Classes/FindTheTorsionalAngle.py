class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return ((self.x * no.x) + (self.y * no.y) + (self.z * no.z))

    def cross(self, no):
        return Points(((self.y * no.z) - (self.z * no.y)),((self.x * no.z) - (self.z * no.x)),((self.x * no.y) - (self.y * no.x)))
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

# Input Format
# One line of input containing the space separated floating number values of the X, Y and Z coordinates of a point.
# Output Format
# Output the angle correct up to two decimal places.
# Sample Input
# 0 4 5
# 1 7 6
# 0 5 9
# 1 7 2
# Sample Output
# 8.19
