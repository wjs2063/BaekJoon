from collections import deque
def solution(target):
    answer = []
    # 최소한의 다트개수와, 싱글 또는 불을 최대한 많이던져라 
    if target == 29:
        return [2,2]
    def bfs(target):
        # 점수,던진횟수,bool개수
        visit = set()
        q = deque([(0,0,0)])
        sub = []
        while q:
            x,cnt,boo = q.popleft()
            if x == target:
                return [cnt,boo]
            # 싱글과,불을 먼저던지자
            if x + 50 <= target and x + 50 not in visit:
                visit.add(x + 50)
                q.append((x + 50,cnt + 1,boo + 1))
            # 싱글
            for i in range(1,20 + 1):
                if x + i <= target and x + i not in visit:
                    visit.add(x + i)
                    q.append((x + i,cnt + 1,boo + 1))
            # 싱글,불을 제외한 더블,트리플 
            for i in range(1, 20 + 1):
                for j in [i*2,i*3]:
                    if x + j <= target and x + j not in visit:
                        visit.add(x + j)
                        q.append((x + j,cnt + 1,boo)) 
    return bfs(target)