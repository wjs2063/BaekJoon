import sys
input = sys.stdin.readline

n = int(input().strip())

schedule = []

for _ in range(n):
    start,end = map(int,input().split())
    schedule.append((start,end))
# 가장 늦게 끝나도 되는 Task 기준으로 정렬
schedule.sort(key = lambda x:-x[1])
# ans := 현재시각
ans = schedule[0][1]
# ti 걸리는시간, si 시간이내에 처리 항상 마감 직전에 모든걸 처리한다고 생각
for ti,si in schedule:
    # 만약 현재 시각이 다음 태스크를 끝내야 할 시각보다 이후라면 그만큼 대기시간 발생
    if ans > si:
        ans -= (ans - si)
    ans -= ti
if ans < 0:
    print(-1)
else:
    print(ans)