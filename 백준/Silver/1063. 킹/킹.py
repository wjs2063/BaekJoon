import sys
input = sys.stdin.readline


x,y,n = input().split()

kx,ky = int(x[-1]) - 1,ord(x[0]) - ord("A")

sx,sy = int(y[-1]) - 1,ord(y[0]) - ord("A")


dirs = {
    "R":(0,1),
    "L":(0,-1),
    "B":(-1,0),
    "T":(1,0),
    "RT":(1,1),
    "LT":(1,-1),
    "RB":(-1,1),
    "LB":(-1,-1)
}

def in_range(x,y):
    return 0 <= x < 8 and 0 <= y < 8

for _ in range(int(n)):
    t = input().strip()
    next_kx,next_ky = kx + dirs[t][0],ky + dirs[t][1]
    # 돌이랑 위치가 같다면
    if (next_kx,next_ky) == (sx,sy):
        #돌도 이동
        next_sx,next_sy = sx + dirs[t][0],sy + dirs[t][1]
        # 범위밖이라면 패스
        if not in_range(next_kx,next_ky) or not in_range(next_sx,next_sy):continue
        kx,ky = next_kx,next_ky
        sx,sy = next_sx,next_sy
    #돌이랑 위치가 다르다면
    else:
        if not in_range(next_kx,next_ky):continue
        kx,ky = next_kx,next_ky

print(chr(ky + ord("A")) + str(kx + 1))
print(chr(sy + ord("A")) + str(sx + 1))
