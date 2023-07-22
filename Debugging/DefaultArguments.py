class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream==None: # add this condition
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())
        

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())


# Debug the given function print_from_stream using the default value of one of its arguments.
# The function has the following signature:
# def print_from_stream(n, stream)
# This function should print the first n values returned by get_next() method of stream object provided as an argument. Each of these values should be printed in a separate line.
# Whenever the function is called without the stream argument, it should use an instance of EvenStream class defined in the code stubs below as the value of stream.
# Your function will be tested on several cases by the locked template code.
# Sample Input 0
# 3
# odd 2
# even 3
# odd 5
# Sample Output 0
# 1
# 3
# 0
# 2
# 4
# 1
# 3
# 5
# 7
# 9
# Explanation 0
# There are 3 queries in the sample.
# In the first query, the function print_from_stream(2, OddStream()) is exectuted, which leads to printing values 1 and 3  in separated lines as the first two non-negative odd numbers.
# In the second query, the function print_from_stream(3) is exectuted, which leads to printing values 2, 4 and 6 in separated lines as the first three non-negative even numbers.
# In the third query, the function print_from_stream(5, OddStream()) is exectuted, which leads to printing values 1, 3, 5, 7 and 9 in separated lines as the first five non-negative odd numbers.
