import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0.
# Sample Input
# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
# Sample Output
# 1
# Explanation
# Here, the root is a feed tag, which has depth of 0.
# The tags title, subtitle, link and updated all have a depth of 1.
# Thus, the maximum depth is 1.
