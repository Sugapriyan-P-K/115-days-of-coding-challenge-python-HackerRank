# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N XM. (N is an odd natural number,M and  is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs
#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
# solved code

n,m = map(int, input().split())
k = (m-3)//2
mat_design = '.|.'
welcome = 'WELCOME'
dash='-'
for i in range(1, (n+1)//2):
    print(str(dash*k+mat_design*(i+i-1)+dash*k).strip())
    k=k-3
print(str(dash*((m-len(welcome))//2)+welcome+dash*((m-len(welcome))//2)).strip())
for i in range(n//2,0,-1):
    k=k+3
    print(str(dash*k+mat_design*(i+i-1)+dash*k).strip())
