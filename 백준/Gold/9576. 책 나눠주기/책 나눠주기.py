import sys
input = sys.stdin.readline

# a 이상 b 이하 책중 남아있는 책한권 골라주기

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    graph = []
    for _ in range(m):
        a,b = map(int,input().split())
        graph.append((a,b))
    booked = [0]*(n + 1)
    ans = 0
    graph.sort( key = lambda x: x[1])
    for a,b in graph:
        for i in range(a,b + 1):
            if booked[i] :continue
            booked[i] = 1
            ans += 1
            break
    print(ans)
