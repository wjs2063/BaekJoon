import sys
import bisect
n=int(input().strip())
sequence=list(map(int,sys.stdin.readline().split()))
dp=[sequence[0]]
for i in range(n):
    if sequence[i]>dp[-1]:
        #dp 의 끝값보다 크다면 
        dp.append(sequence[i])
    else:
        idx=bisect.bisect_left(dp,sequence[i])
        dp[idx]=sequence[i]
print(len(dp))