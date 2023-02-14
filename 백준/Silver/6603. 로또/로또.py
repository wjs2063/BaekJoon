import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(arr,temp,idx):
    global k
    global visited
    if len(temp) == 6:
        print(*temp)
        return
    if idx > len(arr):
        return
    if len(temp) + len(arr) - idx + 1 < 6 :
        return
    for i in range(idx,len(arr)):
        dfs(arr, temp + [arr[i]],i + 1)


    # 현재 idx 를 넣는경우 안넣는경우



while 1:
    arr = list(map(int,input().split()))
    visited = [0]*len(arr)
    if arr[0] == 0 :break
    k = arr[0]
    dfs(arr,[],1)
    print()
