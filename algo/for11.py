import sys
arr1 = list(map(int,sys.stdin.readline().split()));
arr2 = list(map(int,sys.stdin.readline().split()));
arr3 = []

for i in arr2:
    if i < arr1[1]:
        arr3.append(i);

print(' '.join(str(j) for j in arr3));
