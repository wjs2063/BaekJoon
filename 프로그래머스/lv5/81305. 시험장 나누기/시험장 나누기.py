import sys 
sys.setrecursionlimit(10**6)
def solution(k, num, links):
    ans = 0
    
    n = len(links)
    indegree = [0]*(n)
    
    for i,v in enumerate(links):
        l,r = v
        if l != -1:
            indegree[l] += 1
        if r != -1:
            indegree[r] += 1
    root = -1
    for i,v in enumerate(indegree):
        if v == 0:
            root = i
            break
    # root node 를 찾았다.
    sn,en = max(num),sum(num)
    def dfs(root):
        nonlocal cnt 
        l,r = 0,0
        if links[root][0] != -1:
            l += dfs(links[root][0])
        if links[root][1] != -1:
            r += dfs(links[root][1])
        # 자식들의 인원을 다 가져왔어
        # 왼쪽자식과 현재를 합쳤는데 mid를 넘겨?
        if l + r + num[root] <= mid:
            
            return l + r + num[root]
        # 일단 다합치면 넘기는 넘는데
        # 현재와 제일 작은값을 더했을때 안넘으면  1개만 분기
        if num[root] + min(l,r) <= mid:
            cnt += 1
            
            return num[root] + min(l,r)
        
        #싹다 2개분기
        cnt += 2
        return num[root]
        
    
    while sn <= en :
        mid = (sn + en) // 2
        # 모든 그룹은 mid 명 이하로 한다.
        cnt = 1
        dfs(root)
        # 많이 분할됐다? -> 제한이 빡세다 -> 제한을 늘려
        if cnt > k  :
            sn = mid + 1
        else:
            ans =mid
            en = mid - 1
    return ans