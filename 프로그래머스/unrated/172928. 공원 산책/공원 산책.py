def solution(park, routes):
    ans = []
    x,y = 0,0
    d = dict()
    d["E"] = [0,1]
    d["W"] = [0,-1]
    d["N"] = [-1,0]
    d["S"] = [1,0]
    
    n = len(park)
    m = len(park[0])
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x,y, = i,j
    
    for route in routes:
        dirs,cnt = route.split()
        cnt = int(cnt)
        nx,ny = x,y
        f = 1
        while cnt :
            cnt -= 1
            nx += d[dirs][0]
            ny += d[dirs][1]
            if not (0 <= nx < n and 0 <= ny < m) or park[nx][ny] == "X":
                f = 0
                break
        if f:
            x,y = nx,ny
    ans.append(x)
    ans.append(y)
            
    return ans