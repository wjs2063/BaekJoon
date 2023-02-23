import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
l,c = map(int,input().split())

arr = input().split()
arr.sort()

def dfs(idx,temp):
    if len(temp) == l:
        # check
        cnt = 0
        for i in range(len(temp)):
            if temp[i] in ["a","e","i","o","u"]:
                cnt += 1
        if cnt >= 1 and len(temp) - cnt >= 2:
            print("".join(temp))
        return
    for i in range(idx,c):
        dfs(i + 1,temp + [arr[i]])

dfs(0,[])
