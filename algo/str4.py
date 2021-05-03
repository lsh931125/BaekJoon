# 문자열 반복
import sys

n = int(input())
s = []
for i in range(n):
    s.append(list(map(str,sys.stdin.readline().split())))
    for j in s[i][0]:
        print(list(s[i][1])*int(j))