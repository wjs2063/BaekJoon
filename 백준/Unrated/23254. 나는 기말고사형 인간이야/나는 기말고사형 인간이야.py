import sys
from heapq import heappush,heappop


input = sys.stdin.readline

n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

time = 24 * n
h = []
ans = 0
# heap 에 [1시간에 올릴수있는 점수 ,현재점수] 를 넣는다
for i,v in enumerate(A):
    if v + B[i] >= 100 :
        B[i] = 100 - v
    heappush(h,[-B[i],A[i]])

while time :
    possible_add ,score = heappop(h)
    next_score = score - possible_add
    if next_score - possible_add >= 100:
        heappush(h,[-(100 - next_score),next_score])
    else:
        heappush(h,[possible_add,next_score])
    time -= 1
for i,v in enumerate(h):
    ans += v[1]
print(ans)




