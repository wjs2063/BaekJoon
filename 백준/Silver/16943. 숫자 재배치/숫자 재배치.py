import sys
from itertools import permutations
input = sys.stdin.readline

a , b = input().split()
# n!  최대 9! 까지
pp = permutations(a,len(a))

p = list(map("".join,pp))
temp = []
# 0으로 시작하는 애들 제거  + 자기자신 제거
for x in p:
    if x[0] == '0' or x == a:
        continue
    temp.append(int(x))
# temp 가 비어있으면
if not temp:
    print(-1)
else:
    # 정렬하고
    temp.sort()
    answer = -1
    # 순회해서 답찾기
    for x in temp:
        if x < int(b):
            answer = x
        else:
            break
    print(answer)