import sys
input = sys.stdin.readline

t = int(input().strip())

# n = 10
# 1 2 3 4 5  - m = 3 -> 1 2 3, 2 3 4, 3 4 5, 4,5,1 , 5 1 2 ,
# 1 2 3 4 5 6  m = 5 -> 1 2 3 4 5 , 2 3 4 5 6 , 3 4 5 6 1, 4 5 6 1 2 , 5 6 1 2 3, 6 1 2 3 4,
# 1 ~ 5 , 2 ~ 6 ... 6 ~10, 7 ~ 1 ... 10 ~ 4
# prefix sum 활용 ?
# 만약 n = m 이면 1 2 3 4 5 -> 2 3 4 5 1 -> 3 4 5 1 2 -> 등등 이아니라 그냥 1
def solve(bank,m,k):
    n = len(bank)
    answer = 0
    pf_sum = [0] + bank + bank
    if n == m and sum(bank) < k:
        return 1
    for i in range(1,len(pf_sum)):
        pf_sum[i] += pf_sum[i - 1]
    for i in range(1,n + 1):
        sn,en = i , i + m - 1
        if pf_sum[en] - pf_sum[sn - 1] < k :
            answer += 1
    return answer

for _ in range(t):
    n,m,k = map(int,input().split())
    bank = list(map(int,input().split()))
    print(solve(bank,m,k))
