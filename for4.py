import sys
n = int(sys.stdin.readline());

for i in range(1,n+1):
    arr = list(map(int, sys.stdin.readline().split()));
    print(arr[0]+arr[1]);
