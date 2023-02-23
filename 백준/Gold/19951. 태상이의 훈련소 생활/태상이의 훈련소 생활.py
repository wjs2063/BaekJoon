import sys
input = sys.stdin.readline 
n,m = map(int,input().split())

h = list(map(int,input().split()))

order = []
for _ in range(m):
    order.append((list(map(int,input().split()))))

diff = [0]*(n + 1)

for x in order:
    a,b,k = x
    # 시작과 끝만 지정해준다 즉 변화량을 적어두자는 말
    diff[a - 1] += k
    diff[b    ] += -k
for i in range(1,len(diff)):
    diff[i] += diff[i - 1]

for i in range(len(h)):
    h[i] += diff[i]
print(*h)