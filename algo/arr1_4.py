a = 42
num = []
na = []

for i in range(0,10):
    num.append(int(input()));

for j in num:
    na.append(j%a);

na = set(na);
na = list(na);


print(len(na));
