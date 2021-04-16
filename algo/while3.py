num = input();
count = 0;
if len(num) < 2:
    num = '0'+num;
onum = num;

while True:
    sumNum = str(int(num[0]) + int(num[1]));
    if len(sumNum) < 2:
        sumNum = '0'+sumNum;
    num = num[1] + sumNum[1];
    count += 1;
    if num == onum:
        break;
print(count);
