import sys
input = sys.stdin.readline

n,q = map(int,input().split())

visit = set()
# 2k,2k + 1 의 부모는 k 번 mod 연산
for _ in range(q):
    d = int(input().strip())
    x = d
    temp = 0
    while d > 0:
        if d in visit:
            temp = d
        # d를 2로나눠
        d //= 2
        # 만약 루트노드까지 막힘없이 거슬러갔다면?
        if temp == 0:
            visit.add(x)
    print(temp)