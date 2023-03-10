from collections import deque
def solution(stones, k):
    q = deque([])
    ans = []
    # q 에는 인덱스정보담기 , 현재값이상의 인덱스만 저장한다.
    for i,v in enumerate(stones):
        # 현재 v 라는 값보다 작으면 모조리 뺴자
        while q and stones[q[-1]] < v:
            q.pop()
        q.append(i)
        
        if q[0] == i - k:
            q.popleft()
            
        if i >= k - 1:
            ans.append(stones[q[0]])
    return min(ans)