import operator
def person_lister(f):
    def inner(people):
        l=[]
        people = sorted(people,key=lambda x:int(x[2]),reverse = False)
        for p in people:
            l.append(f(p))
        return l
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# Let's use decorators to build a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. 
# Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, 
# print them in the order of their input.
# For Henry Davids, the output should be:
# Mr. Henry Davids
# For Mary George, the output should be:
# Ms. Mary George
# Sample Input
# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F
# Sample Output
# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle
# Concept
# For sorting a nested list based on some parameter, you can use the itemgetter library. You can read more about it here.
