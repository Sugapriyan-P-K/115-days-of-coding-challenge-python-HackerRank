if __name__ == '__main__':
    marksheet=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name,score])
    second_mark = sorted(set([marks for name, marks in marksheet]))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_mark]))
    
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
