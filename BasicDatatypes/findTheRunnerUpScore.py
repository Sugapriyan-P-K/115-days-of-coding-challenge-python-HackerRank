if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    maximum = max(arr)
    arr.remove(maximum)
    print(max(arr))
