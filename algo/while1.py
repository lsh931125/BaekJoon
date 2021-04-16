import sys
arr = list(map(int, sys.stdin.readline().split()));
while arr[0] and arr[1] != 0: 
    print(arr[0]+arr[1]);
    arr = list(map(int, sys.stdin.readline().split()));
