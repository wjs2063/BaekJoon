import sys
input = sys.stdin.readline

n = int(input())


for i in range(n):
    board = list(map(int,input().split()))
    if i == 0 :
        max_dp = board
        min_dp = board
        a,b,c = board
        d,e,f = board
    else:
        a = max(max_dp[0],max_dp[1]) + board[0]
        b = max(max_dp) + board[1]
        c = max(max_dp[1],max_dp[2]) + board[2]
        max_dp = [a,b,c]
        d = min(min_dp[0],min_dp[1]) + board[0]
        e = min(min_dp) + board[1]
        f = min(min_dp[1],min_dp[2]) + board[2]
        min_dp = [d,e,f]


print(max(max_dp),min(min_dp))
