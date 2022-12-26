import sys
input = sys.stdin.readline

n,k = map(int,input().split())

larva = list(map(int,input().split()))
# 부분합이 k이상인것, 어떤것이 더 높은 에너지를 축적할수있을지 어떻게? memozation ?
# dp[x] := x 까지의 최대 축적 에너지
def sol(larva,n,k):
    s = 0
    sn, en = 0,0
    dp = [0]*n
    temp = 0
    for sn in range(n):
        # 항상 sn <= en 만족하게 만들기
        if en < sn :
            en = sn
        # 합 s 가 k 보다 작고, 인덱스범위 안에있다면
        while s < k and en < n:
            s += larva[en]
            en += 1
        dp[en - 1] = max(dp[en - 1],temp + s - k)
        
        temp = max(dp[sn],temp)
        # sn 을 한칸 증가시킬작업
        s -= larva[sn]
    return temp



print(sol(larva,n,k))
