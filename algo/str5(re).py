# 단어 공부
import sys

word = list(str(sys.stdin.readline()).upper())
wordLen = len(word)
cnt = ['']*wordLen

for i in range(wordLen):
    cnt[i] = word.count(word[i])

cntMax = max(cnt)
cntMaxCount = cnt.count(cntMax)

if cntMax < cntMaxCount:
    print("?")
elif cntMax == cntMaxCount:
    manyWord = word[cnt.index(cntMax)]
    print(manyWord)
