import sys
n = int(input());
score = list(map(int,sys.stdin.readline().split()));
top = max(score);
newScore = [];


for i in score:
    newScore.append(i/top*100);

    
print(sum(newScore)/n);
