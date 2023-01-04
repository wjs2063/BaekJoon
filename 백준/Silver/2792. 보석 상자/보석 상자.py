import sys
input = sys.stdin.readline

# 질투심 := 가장 많은 보석을 가지고 있는 학생의 보석수

n,m = map(int,input().split())

# 학생은 항상 같은 보석만 가져간다.
jewelry = [0]*(m + 1)
#jewelry[x] := x 번색상의 개수

for i in range(1, m + 1):
    jewelry[i] = int(input().strip())
# an := n 번째 학생이 받는 보석의 개수

# a1 + a2 + a3 + . . . an = sum(jewerly) = m
# 완탐은 음이아닌 정수의 (a1,a2,a3. . .an) 의  순서쌍
# n H m -> n + m - 1 C m 가지수이므로 시간초과

# 이.탐?
jj = sum(jewelry)
# jj = jewelry 의 총합 최대 3*10^14 개
sn , en = 1,sum(jewelry)
# 질투심의 범위 1 <= 질투심 <= sum(jewerly)
ans = int(1e18 + 1)
# O(M log jj의 최댓값)
while sn <= en :
    mid = (sn + en) // 2
    # s 에는 보석을 받는 학생의 수
    s = 0
    #모든사람이 최대 mid 개를 받을수있다고 가정하고 가능한지 check
    #모든종류의 보석들을 다 나누어 줄수있어야한다.
    #결국 보석의 종류 입장에서는 학생한테 결국 1번은 속해야함
    for i in range(1,m + 1):
        q,r = divmod(jewelry[i],mid)
        # 보석1개가 남으면 누군가한테 주어야함 -> 학생은 여러보석을 가질수없음
        if r == 0:
            s += q
        else:
            s += q + 1
    # 보석이 너무적어 나누어주어야할 학생이 많으면
    if s > n :
        sn = mid + 1
    else:
        en = mid - 1
        ans = mid


print(ans)
