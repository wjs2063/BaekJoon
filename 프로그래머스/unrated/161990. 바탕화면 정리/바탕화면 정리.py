def solution(wallpaper):
    answer = []
    n = len(wallpaper)
    m = len(wallpaper[0])
    INF = int(1e4)
    lux,luy,rdx,rdy = INF,INF,0,0
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                lux = min(lux,i)
                luy = min(luy,j)
                rdx = max(rdx,i + 1)
                rdy = max(rdy,j + 1)
            
    return  [lux,luy,rdx,rdy]