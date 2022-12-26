import sys
input = sys.stdin.readline

n,t = map(int,input().split())

people = []

for _ in range(n):
    l,r = map(int,input().split())
    people.append((l,r))

# 사람들의 최소주량을 다더했는데 총량 t 를 넘거나 최대주량을 다더했는데 t 미만이면 처음부터 불가능
# O(N)
if sum([x[0] for x in people]) > t or sum([x[1] for x in people]) < t :
    print(-1)
else:
    # O(Nlogn)
    #0<= x <= 1e9 를 돌면서
    sn,en = 0, int(1e9)
    ans = int(1e10)
    while sn <= en :
        mid = (sn + en) // 2
        cnt = 0
        temp = 0
        for l,r in people:
            if mid > r:
                cnt += 1
                temp += r
            elif mid >= l :
                cnt += 1
                temp += mid
        # 모든사람이 정상적으로 술 받을수있거나
        if cnt == n and temp >= t:
            ans = min(ans,mid)
            en = mid - 1
        elif cnt < n  or temp < t:
            sn = mid + 1
    print(ans)