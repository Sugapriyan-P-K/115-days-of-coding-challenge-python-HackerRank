

# Sample Input
# 6
# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
# Sample Output
# 5
# Explanation
# The feed and subtitle tag have one attribute each - lang.
# The title and updated tags have no attributes.
# The link tag has three attributes - rel, type and href.
# So, the total score is 1 + 1 + 3 = 5.
# NOTE: In order to parse and generate an XML element tree, use the following code:
# >> import xml.etree.ElementTree as etree
# >> tree = etree.ElementTree(etree.fromstring(xml))
# Here, XML is the variable containing the string.
# Also, to find the number of keys in a dictionary, use the len function:
# >> dicti = {'0': 'This is zero', '1': 'This is one'}
# >> print (len(dicti))
# 2
