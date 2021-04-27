n = int(input())
ox = []
sum = 0
bonus = 1

for i in range(n):
    ox.append(list(input()))
    for k in ox[i]:
        if k == 'O':
            sum += bonus
            bonus += 1
        else:
            bonus = 1;
    print(sum)
    sum = 0
    bonus = 1
