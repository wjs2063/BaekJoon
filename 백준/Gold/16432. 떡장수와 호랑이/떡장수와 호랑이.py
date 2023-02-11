import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())
info = defaultdict(list)
for i in range(n):
    info[i + 1].extend(list(map(int,input().split()))[1:])
# info[x] := x 번쨰날의 떡 리스트

rice = [[0]*10 for _ in range(n + 1)]
# rice[x][t] -> x 번째날에 t라는 떡을 먹었을때 1 , 아니면 0
flag = False
def dfs(days,past,yester):
    # 마지막날까지 무사히왔으면
    global flag
    if flag :return
    # n번째날짜까지 왔으면 종료
    #print(past,yester)
    if days == n + 1 :
        flag = True
        for x in past:
            print(x)
        return
    for x in info[days]:
        # 이전에 먹었던 떡이라면 날짜와 x 라는 상태
        if x == yester or  rice[days][x]: continue
        rice[days][x] = 1
        dfs(days + 1,past + [x],x)
dfs(1,[],-1)
if not flag:
    print(-1)