import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

b = []
hp = [[0]*n for _ in range(n)]
for _ in range(n):
    b.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if 1 <= b[i][j] <= 9:
            hp[i][j] = b[i][j]


shot = list(map(int,input().split()))

ans = 0

def go(i):
    for j in range(n):
        if b[i][j] > 0:
            return i,j
    return -1,-1

def in_range(x,y):
    if 0 <= x < n and 0 <= y < n: return 1
    return 0

def dfs(idx,score):
    global ans
    if idx >= k:
        ans = max(ans,score)
        return

    for i in range(n):
        """
        i번째 행을 선택했을때 가장 처음 관통하는 총알의 좌표를 반환해야함
        """
        x,y = go(i)
        s = 0
        b_path = []
        h_path = []
        # 현재 행에 총알이 있어?
        if (x,y) != (-1,-1):
            # 보너스 점수라면?
            if b[x][y] >= 10 :
                s += b[x][y]
                # 이전 좌표와 값을 저장해
                b_path.append([x,y,b[x][y]])
                #변경해
                b[x][y] = 0
            # 일반 표적이라면
            elif 1 <= b[x][y] < 10:
                # 총알공격력만큼 감소
                # 감소하기 이전 좌표정보 저장해
                b_path.append([x,y,b[x][y]])
                b[x][y] -= shot[idx]
                # 체력이 다 소진됐으면
                if b[x][y] <= 0 :
                    s += hp[x][y]
                    # 4방향에 대해서
                    for nx,ny in [(x + 1,y),(x - 1,y),(x,y - 1),(x,y + 1)]:
                        if not in_range(nx,ny):continue
                        if b[nx][ny] > 0:continue
                        # 이전 정보 저장하고
                        h_path.append([nx,ny,hp[nx][ny]])
                        b_path.append([nx,ny,b[nx][ny]])
                        hp[nx][ny] = hp[x][y] // 4
                        b[nx][ny] = hp[nx][ny]
        dfs(idx + 1,score + s)
        for x,y,val in b_path:
            b[x][y] = val
        for x,y,val in h_path:
            hp[x][y] = val
dfs(0,0)
print(ans)
