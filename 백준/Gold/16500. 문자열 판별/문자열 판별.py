import sys
input = sys.stdin.readline

S = input().strip()

n = int(input())

words = []


for _ in range(n):
    words.append(input().strip())
answer = False

"""
시간초과 코드 

def dfs(S,index):
    global words
    global answer
    # 끝까지 왔으면 종료
    if index >= len(S):
        answer = True
        return
    for word in words:
        # dfs 탐색해서 정답임을 확인했으면 종료
        if answer :
            return
        # 현재 인덱스부터 word 까지 같으면 dfs
        if S[index:index + len(word)] == word:
            dfs(S,index + len(word))
dfs(S,0)

if answer :
    print(1)
else:
    print(0)

반례 
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

aa
aaaa 
aaaaaa
aaaaaaaa

"""

# dp[i] := 문자열 S의 i번쨰 인덱스까지  문자열을 만들수있는가? T or F
n = len(S)
dp = [False]*(n)
# 공간복잡도 O(N)
# 초기값


for word in words:
    if len(word) <= len(S) and S[:len(word)] == word :
        dp[len(word) - 1] = True

# O(n^2)
for i in range(1,n):
    for word in words:
        # i - 1 번째까지 인덱스를 만드는게 가능했으면 다음 i : i + len(word) 까지 체크
        if i + len(word) <= len(S) and dp[i - 1] and S[i:i + len(word)] == word :
            dp[i + len(word) - 1] = True
if dp[n - 1]:
    print(1)
else:
    print(0)

'''
Test case
s
1
s
output : 1

sssss
2
ssss
ss
output : 0

airflow
3
a
irf
low
output 1

'''