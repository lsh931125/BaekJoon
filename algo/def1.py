import sys

a = list(map(int,sys.stdin.readline().split()))
def solve(a: list) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum

sum = solve(a)
print(sum)