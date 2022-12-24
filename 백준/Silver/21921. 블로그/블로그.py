import sys
input = sys.stdin.readline

n,x = map(int,input().split())

visitor = [0] + list(map(int,input().split()))
def sol(visitor):
    for i in range(1,len(visitor)):
        visitor[i] += visitor[i - 1]
    max_visit = 0

    for i in range(1, len(visitor) - x + 1):
        max_visit = max(max_visit,visitor[i + x - 1 ] - visitor[i - 1])
    cnt = 0

    for i in range(1,len(visitor) - x + 1):
        if visitor[i + x - 1] - visitor[i - 1] == max_visit:
            cnt += 1
    return max_visit,cnt

if max(visitor) == 0:
    print("SAD")
else:
    r1,r2 = sol(visitor)
    print(r1)
    print(r2)