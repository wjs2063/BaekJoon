import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))


top = [None,arr,[],[]]
pos,sub = 1,2
ans = []
while n :
    # pos 배열의 끝이 n 이아니면 계속 패스
    while top[pos]:
        # 크기가 n 인 원판이면
        if top[pos][-1] == n :
            top[pos].pop()
            ans.append([pos,3])
            n -= 1
        else:
            ans.append([pos,sub])
            top[sub].append(top[pos].pop())
    pos,sub = sub,pos

print(len(ans))
for x in ans:
    print(*x)