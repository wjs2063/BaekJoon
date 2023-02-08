from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    q = deque([(x,y,"",0)])
    dt = [(1,0,'d'),(0,-1,'l'),(0,1,'r'),(-1,0,'u')]
    # 일단 먼저 r,c 에보내기
    while q:
        x,y,path,cnt = q.popleft()
        if (x,y) == (r,c) and (k - cnt ) % 2 == 1:
            return "impossible"
        if (x,y) == (r,c) and cnt == k:
            return path
        for i in range(4):
            dx,dy,direction = dt[i]
            nx = x + dx
            ny = y + dy
            if nx <= 0 or nx > n or ny <= 0 or ny > m: continue
            if abs(nx - r) + abs(ny - c) + cnt + 1 > k:continue
            q.append((nx,ny,path + direction,cnt + 1))
            break

    
    return "impossible"