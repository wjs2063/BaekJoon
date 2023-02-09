from collections import deque
def solution(x, y, n):
    def bfs(x,y,n):
        q = deque([(x,0)])
        visited = set()
        visited.add(x)
        while q:
            x,cnt = q.popleft()
            if x == y :return cnt
            if x + n <= y and x + n not in visited:
                q.append((x + n,cnt + 1))
                visited.add(x + n)
            if 2*x <= y and 2*x not in  visited:
                q.append((2*x,cnt + 1))
                visited.add(2*x)
            if 3*x <= y and 3*x not in visited:
                visited.add(3*x)
                q.append((3*x,cnt + 1))
        return -1
        
    return bfs(x,y,n)