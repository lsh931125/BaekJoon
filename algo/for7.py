import sys
a = int(sys.stdin.readline())
for i in range(1,a+1):
    arr = list(map(int, sys.stdin.readline().split()));
    print(f'Case #{i}: {arr[0] + arr[1]}');
    
