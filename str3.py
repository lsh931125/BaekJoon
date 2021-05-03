# 알파벳 찾기
S = list(input())
ran = []
pri = []
for i in range(97,123):
    ran.append(chr(i))
for j in ran:
    if j not in S:
        pri.append(-1)
    elif j in S:
        pri.append(S.index(j))
print(*pri, sep = ' ') # 대괄호 없이 출력