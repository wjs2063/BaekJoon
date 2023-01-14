import sys
input = sys.stdin.readline

n = int(input())
answer = 0
cc = list(map(int,input().split()))


# 투포인터???
# 1이면 + 2이면 -  로 두고 계산한다.
# 압축시켜서 계산하자
# 연속된것은 다 뭉쳐서 계산하자 예를들면 1 1 2 2 -> +2 ,-2 로 두자는 이야기다.

stack = [cc[0]]
idx = 0
dx = []
dir = 1
for i in range(1,n):
    #같은것들이면  추가
    if stack[-1] == cc[i]:
        stack.append(cc[i])
    else:
        #다른것들이라면?
        if stack[-1] == 1:
            dx.append(len(stack))
        else:
            dx.append(len(stack))
        # 갱신해주고 초기화시켜준다
        stack = [cc[i]]
if stack and stack[-1] == 1:
    dx.append(len(stack))
else:
    dx.append(len(stack))
# 자 dx 에는 압축된 좌표가 들어가있다.
# 연속된 부분합의최댓값을 찾아보자 ( 사실 부분합의 절댓값의 최댓값으로 보는게 맞다 )( 1은 - 2는 + 로생각하거나 그반대로)

dp = [0]*(len(dx) + 1 )
dp1 = [0]*(len(dx) + 1)
ans = 0
# 그냥 홀짝 합이 다르다
# 첫스타트는 1로해보자
dir = 1
# dp[i][0] -> 음수일떄
# dp[i][1] -> 양수일떄

# dp[3] = a0 + a1 + a2 + a3 , a1 + a2 + a3 , a2 + a3 , a3 이므로
# a3 을 제외하고생각해보면 = dp[2] + a3 이되는거아닌가 근데 이 dp[2]가 음수일수도있고 양수일수도있다 .
answer = 0
dir1 = 1
dir2 = -1
for i in range(1,len(dx) + 1):
    # dp[i] := i번째인덱스를 오른쪽끝으로하는 부분합
    # 만약 dp[i] 가 음수면
    dp[i] = max(dp[i - 1] + dir1*dx[i - 1],dir1*dx[i - 1])
    dp1[i] = max(dp1[i - 1] + dir2*dx[i - 1],dir2*dx[i - 1])
    dir1 = -dir1
    dir2 = -dir2
print(max(max(dp),max(dp1)))




"""
1 1 2 1 1 -> 답은 3임
1 2 2 1 2 1 1 2 1 1 -> 답 3
2 2 1 2 -> 답 2 
2 2 2 2 2 1 1 2 2 2  -> 답 6 

i ~ j 까지 중 1의 개수와 2의개수의 차이 

9
1 2 1 2 1 1 1 2 2 -> 답 3

9
2 1 2 1 1 1 1 2 2 -> 4 

"""