import sys

a = int(sys.stdin.readline());
b = int(sys.stdin.readline());
c = int(sys.stdin.readline());

x = list(str(a*b*c));

for i in range(0,10):
    print(x.count(str(i)));
