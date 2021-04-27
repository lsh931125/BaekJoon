# 클린코드로 만들어보기.
import sys

n = int(input())
score = []
cnt = []

for i in range(n):
    a=0
    avg = 0
    sum = 0 
    up = 0
    score.append(list(map(int,sys.stdin.readline().split())))
    cnt.append(score[i][0])
    del score[i][0]
    for j in score[i]:
        a = a+j
    sum = a
    avg = a/cnt[i]
    for k in score[i]:
        if k > avg:
            up += 1
    print(str(format(up/cnt[i]*100,".3f"))+"%")