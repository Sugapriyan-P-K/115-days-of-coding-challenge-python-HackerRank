class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        return Complex((self.real * no.real) - (self.imaginary * no.imaginary), (self.real * no.imaginary) + (self.imaginary * no.real))

    def __truediv__(self, no):
        return Complex(((self.real * no.real) + (self.imaginary * no.imaginary))/(no.real**2 + no.imaginary**2),((self.imaginary * no.real) - (self.real * no.imaginary)) / (no.real**2 + no.imaginary**2))
    

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

# Sample Input
# 2 1
# 5 6
# Sample Output
# 7.00+7.00i
# -3.00-5.00i
# 4.00+17.00i
# 0.26-0.11i
# 2.24+0.00i
# 7.81+0.00i
# Concept
# Python is a fully object-oriented language like C++, Java, etc. For reading about classes.
# Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.
# __add__-> Can be overloaded for + operation
# __sub__ -> Can be overloaded for - operation
# __mul__ -> Can be overloaded for * operation
