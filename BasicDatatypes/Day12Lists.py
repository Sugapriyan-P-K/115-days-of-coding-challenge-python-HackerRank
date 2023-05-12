if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        args = input().strip().split(" ")
        if args[0] == "append":
            list.append(int(args[1]))
        elif args[0] == "insert":
            list.insert(int(args[1]), int(args[2]))
        elif args[0] == "print":
            print(list)
        elif args[0] == "remove":
            list.remove(int(args[1]))
        elif args[0] == "sort":
            list.sort()
        elif args[0] == "pop":
            list.pop()
        elif args[0] == "reverse":
            list.reverse()
            
   
# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
