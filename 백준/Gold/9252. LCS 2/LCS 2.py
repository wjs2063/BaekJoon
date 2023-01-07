import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
n,m = len(A),len(B)
#dp[i][j] : i 는 A 문자열인덱스 , j 는 B 문자열 인덱스
#dp[i][j] := A문자열을 i번쨰인덱스까지, B문자열을 j번쨰 인덱스까지 확인했을때 LCS 길이 (최장길이)
dp = [[0]*(m + 1) for _ in range(n + 1)]

for i in range(1,n + 1):
    for j in range(1,m + 1):
        # 경계선
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 다르다면 이전의 dp 값들중 큰값으로 유지한다
        else:
            dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
# T: O(N^2)  S:O(N^2)
# dp 값은 구했는데 문자열은 어떻게??
# 처음으로 dp 값이 증가하는 부분만 골라서 넣기
answer = ""
val = 0
# 틀린 코드
"""
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if dp[i][j] > val:
            #갱신해주고
            val = dp[i][j]
            answer += B[j - 1]
"""
# 역으로 계산해줄떄는
cnt = dp[n][m]
x,y = n,m
while cnt  :
    # dp중에 cnt값을가진 애들중 왼쪽인덱스 값을 찾자
    # x + 1, y + 1 인데 y + 1 보다 1칸 왼쪽을 계속 살펴보는것
    if dp[x - 1][y] == cnt - 1 and dp[x][y - 1] == cnt - 1:
        answer += A[x - 1]
        cnt -= 1
        x -= 1
        y -= 1
    else:
        if dp[x][y - 1] > dp[x - 1][y]:
            y -= 1
        else:
            x -= 1


if dp[n][m] == 0:
    print(dp[n][m])
else:
    print(dp[n][m])
    print(answer[::-1])


"""
test case 
DDDDDZZZAAA
ZZZAAA
답
6
ZZZAAA

AAAA
AAAA
답
4
AAAA

DBCA
BCAD
답
2
BCA



"""