import sys
from itertools import product
input = sys.stdin.readline
a,b = map(int,input().split())


# 9자리숫자
# 4와 7을
answer = []
for i in range(1,10):
    pp = product(["4","7"],repeat = i)
    for p in pp:
        x = "".join(p)
        answer.append(x)

res = 0

for x in answer:
    if a <= int(x) <= b:
        res += 1
print(res)