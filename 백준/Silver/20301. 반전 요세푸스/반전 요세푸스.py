import sys
input = sys.stdin.readline

n,k,m = map(int,input().split())

arr =  [i for i in range(1, n + 1)]

idx = -1

direction = 1
answer = []
cnt = 0
while arr:
    if len(arr) == 1:
        answer.append(arr[0])
        break
    if direction == 1:
        # 방향 돌리기
        idx += k
        idx %= len(arr)
        # 제거
        answer.append(arr.pop(idx))
    else:
        # 방향돌리기
        idx -= k
        idx %= len(arr)
        # 제거
        answer.append(arr.pop(idx))
    cnt += 1
    if cnt >= m :
        cnt = 0
        direction = -direction
    # 정방향이면
    if direction == 1:
        idx = (idx - 1) % len(arr)
    else:
        idx = (idx) % len(arr)

for x in answer:
    print(x)