import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    build_time=[0]+list(map(int,input().split()))
    build_order=[[] for _ in range(N+1)]
    dp=[0 for _ in range(N+1)]
    degree=[0 for _ in range(N+1)]
    for _ in range(K):
        prev,next=map(int,input().split())
        build_order[prev].append(next)
        degree[next]+=1
        
    last=int(input())
    queue=deque()
    for i in range(1,N+1):
        if degree[i]==0:
            queue.append(i)
            dp[i]=build_time[i]
    while queue:
        x=queue.popleft()
        for j in build_order[x]:
            degree[j]-=1
            dp[j]=max(dp[x]+build_time[j],dp[j])
            if degree[j]==0:
                queue.append(j)
        
    #마지막건물 더해주기 포함안시켰음 build_order 에
    
    print(dp[last])