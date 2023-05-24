import string
def print_rangoli(size):
    alphabet  = list(string.ascii_lowercase)
    dash = '-'
    l1 = alphabet[0:size]
    l1 = '-'.join(l1)
    l2 = l1[::-1]
    m,n=size,size
    x=0
    for i in range(1, n):
        print(str(dash*((n+n-(2*i)))+l2[:i+i-1]+l1[m+m-1:]+dash*((n+n-(2*i)))))
        m-=1
    print(l2[:len(l2)-1]+l2[::-1])
    for i in range(n-1,0,-1):
        print(str(dash*((n+n-(2*i)))+l2[:i+i-1]+l1[(x+x+1)+2:]+dash*((n+n-(2*i)))))
        x+=1
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

#size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
