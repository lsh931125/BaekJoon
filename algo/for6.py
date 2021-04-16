import sys
a = int(sys.stdin.readline())
b = [];
for i in range(1,a+1):
    b.append(i);

b.reverse();
for j in range(0,a):
    print(b[j]);
