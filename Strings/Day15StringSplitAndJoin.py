def split_and_join(line):
    # write your code her
    res = list(line)
    line = ""
    for i in range(len(res)):
        if res[i]==' ':
            line += '-'
        else:
            line += res[i]
    return line
        
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
# Joining a string is simple:

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 
# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
