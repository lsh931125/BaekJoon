# 다시해보기
import sys
arrNum = []

for count in range(9):
    arrNum.append(int(input()));

print(max(arrNum));
print(arrNum.index(max(arrNum))+1);