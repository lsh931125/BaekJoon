num = []
sumNum = []
selfNum = []

def d(a):
    num = list(map(int,str(a)))
    global sum
    sum = a
    for i in num:
        sum += i
    return sum

for i in range(1,10000):
    d(i)
    num.append(i)
    sumNum.append(sum)
selfNum = list(set(num)-set(sumNum))
selfNum.sort()

for i in selfNum:
    print(i)
