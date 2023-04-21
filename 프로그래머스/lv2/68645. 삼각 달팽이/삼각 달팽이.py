def solution(n):
    dirs = [[1,0],[0,1],[-1,-1]]
    d = 0
    ans = [[0] * i for i in range(1,n + 1)]
    item = 1
    x,y = -1,0
    cnt = (n * (n + 1)) // 2
    while cnt :
        nx,ny = x + dirs[d][0] , y + dirs[d][1]
        if nx < 0 or nx >= n or ny < 0 or ny > nx or ans[nx][ny] != 0:
            d = (d + 1) % 3
            continue
        x,y = nx,ny
        ans[x][y] = item
        item += 1
        cnt -= 1
    answer = []
    for i in range(n):
        answer.extend(ans[i])
        
    return answer