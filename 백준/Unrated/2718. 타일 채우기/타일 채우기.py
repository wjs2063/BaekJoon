import sys
input = sys.stdin.readline


t = int(input())

"""
문제 해결전략

dp[n] = dp[n - 1] + dp[n - 2] + 2*(dp[n - 2] + dp[n - 3] ... dp[n - n])
+ dp[n - 2] + dp[n - 4] + dp[n - 6] ... 이다 
이는 끝점을 기준으로 생각해볼수있다.
끝점에서 2*1 을 한개도 사용하지않는경우, 2*1 을 1개만 사용하는경우, 2*1을 2개사용하는경우 로 나눈다.
즉 | 와 ㅡ 를 사용할텐데
CASE 1 -> 2*1 을 2개사용하는경우 dp[n - 1]
  |
  |

CASE 2 ->  2*1 을 1개만사용하는경우
    ㅡ
     |
    ㅡ
와 같은경우 저기 중앙에 |를 채워넣는경우 dp[n - 2] 가될것이고 ㅡ 를 넣는다면 다시 분기를한다.
즉 dp[n - 2 ] + dp[n - 4] ...

     |
    ㅡ
    ㅡ          와 같은경우는 위에 | 를 넣어서 dp[n - 2] 를 만들거나 ㅡ 를 넣어서 dp[n - 3]을 만들거나 등등
    즉 dp[n - 2] + dp[n - 3] + dp[n - 4] ... 로 둔다. 상하 대칭이므로 * 2 배

CASE 3 -> 2*1 을 1개도 사용하지않는경우 dp[n - 2] 

종합하면 
dp[n] = dp[n - 1] + dp[n - 2] + 2*(dp[n - 2] + dp[n - 3] ... ) + dp[n - 2] + dp[n - 4]... 이다
 
"""

def solve(n):
    dp = [0] *(n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        for k in range(2,n + 1):
            if i - k >= 0:
                dp[i] += 2*dp[i - k]
        for k in range(2,n + 1,2):
            if i - k >= 0:
                dp[i] += dp[i - k]
    return dp[n]

for _ in range(t):
    n = int(input())
    print(solve(n))
