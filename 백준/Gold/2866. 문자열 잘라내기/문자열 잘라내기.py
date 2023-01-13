import sys
input = sys.stdin.readline


r,c = map(int,input().split())

words = []

for _ in range(r):
    words.append(input().strip())
# 시작점 0 끝점 r
sn,en = 0,r - 1
answer = 0

# sn <= en 으로 설정
while sn <= en:
    # mid := 위에서부터 몇번 커팅하는지를 담은변수
    mid = (sn + en) // 2
    # mid + 1행부터 끝까지 세로로 zip 으로 묶어준다
    # 0번쨰부터 mid 행까지 커팅이므로 mid + 1 부터 체크해야함
    x = list(map("".join,(zip(*words[mid:]))))
    # mid 행부터 끝까지 했을때 겹치는 문자가없어? 행을 더 높혀보자 ( 더커팅할수있다는소리)
    if len(set(x)) == c:
        answer = mid
        sn = mid + 1
    # 겹치는게있어? 그러면 행을 더 낮게가져가자 ( 커팅 너무많이한거같으니 줄여야함)
    else:
        en = mid - 1
print(answer)