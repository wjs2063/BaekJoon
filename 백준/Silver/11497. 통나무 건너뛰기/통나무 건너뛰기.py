import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input())
    temp = [0]*n
    arr = list(map(int,input().split()))
    arr.sort()
    # 지그재그로
    for i,v in enumerate(arr):
        if i % 2 == 0 :
            temp[i // 2] = v
        else:
            temp[-(i // 2 + 1)] = v
    # 0 이면 0번째 index, 1이면 -1 번째 인덱스 2 이면 1번째 3 이면 -2 번째인덱스
    ans = 0
    for i in range(n - 1):
        # i - 1번째와 i + 1 번째
        ans = max(ans,abs(temp[i] - temp[i - 1]),abs(temp[i] - temp[i + 1]))
    print(ans)

