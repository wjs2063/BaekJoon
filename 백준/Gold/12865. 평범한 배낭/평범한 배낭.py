import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,k = map(int,input().split())

bag = [[-1,-1]]

for _ in range(n):
    w,v = map(int,input().split())
    bag.append((w,v))
dp = [[-1]*(n + 1) for _ in range(k + 1)]
# dp[w][n] := w를 담을수있는가방에 n 개를 담아서 얻을수있는 최대 가치


# pack(weight,item) -> 현재 item번호, weight 으로 얻을수있는 최대 가치
def pack(weight,item):
    # 모든 경우는 현재 item 을 넣거나 말거나 이다
    if weight <= 0 or item > n : return 0
    ret = dp[weight][item]
    # 이미 계산한 경우면
    if ret != -1:
        return ret
    # 현재 아이템을 넣지않는경우, 그리고 현재 아이템을 넣을경우
    dp[weight][item] = pack(weight,item + 1)
    # 현재 item 을 넣을수있는경우
    if weight - bag[item][0] >= 0:
        dp[weight][item] = max(dp[weight][item],pack(weight - bag[item][0],item + 1) + bag[item][1])
    return dp[weight][item]

pack(k,1)
print(max(dp[k]))