import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
cc = [0]*(10**6 + 1)
tt = [0]*(10**6 + 1)
h = []

for _ in range(n):
    x,y = map(int,input().split())
    heapq.heappush(h,[x,y])
    cc[x] += 1
    cc[y] -= 1
for i in range(1,10**6 + 1):
    cc[i] += cc[i - 1]
t = max(cc)
seat = [0] * (t + 1)
av = [i for i in range(1, t + 1)]
heapq.heapify(av)
# rt := 반납 시간 rt[0][0] [0][1] -> 반납시간,반납좌석
rt = []
while h :
    while rt and rt[0][0] < h[0][0]:
        x,y = heapq.heappop(rt)
        heapq.heappush(av,y)
    st,en = heapq.heappop(h)
    # 사용가능좌석
    s = heapq.heappop(av)
    seat[s] += 1
    # 사용최대 시각 , 번호 저장
    heapq.heappush(rt,(en,s))
print(t)
print(*seat[1:])