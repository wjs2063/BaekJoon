import sys
input = sys.stdin.readline

n,m = map(int,input().split())

money = []

for _ in range(n):
    money.append(int(input().strip()))

sn,en = min(money),sum(money)
ans = 0
# 돈이남아도 다넣고 다시 k 원을 뺴내는과정을 거치므로
# 수중에있는돈은 최대 k원임을 알수있다.
while sn <= en :
    mid = (sn + en) // 2
    cnt = 0
    temp = 0
    flag = False
    # k 를 최소화 하려면 최대한 횟수카운팅을 많이해서 범위를 줄여보는게좋음
    for i in range(len(money)):
        # 하루를 살수없으므로 돈을 늘려야함
        if mid < money[i]:
            flag = True
            break
        # 수중에있는돈으로 불가능하면 다시인출
        if temp < money[i]:
            temp = mid
            cnt += 1
        temp -= money[i]
    # 만약 하루를 살수없거나 너무 자주인출하면
    if flag or cnt > m :
        sn = mid + 1
    # 많이 인출해야한다면 넉넉하게 늘려
    elif cnt <= m:
        en = mid - 1
        ans = mid
print(ans)
