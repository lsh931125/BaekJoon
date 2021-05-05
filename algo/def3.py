# https://nanarin.tistory.com/161

N = int(input())
hanNum = []

# 한수를 구하는 함수
# def han(a):

for i in range(1,N+1):
    if i < 100:
        hanNum.append(i)
    elif i >= 100:
        numLen = len(str(i))
        num = []
        for j in list(map(int,str(i))):
            num.append(j)
        if num[1]-num[0] == num[2]-num[1]:
            hanNum.append(i)

print(len(hanNum))
