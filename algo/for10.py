import sys

a = int(sys.stdin.readline());

for i in range(1, a+1):
    print(f'%{a}s' % f'{"*"*i}');
