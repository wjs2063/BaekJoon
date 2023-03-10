import sys
input = sys.stdin.readline

A,B = input().split()
ans = 100

"""
문제해결전략
A := a1a2a3
B := b1b2b3b4b5
슬라이딩윈도우 방식으로 b1b2b3, b2b3b4,b3b4b5 와 A 와 비교한후최소차이를찾는다
어차피 다른부분은 추가해서 같게만들수있기때문이다
"""

for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1
    ans = min(ans,cnt)
print(ans)
