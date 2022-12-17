import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
S = input().strip()
T = input().strip()
ans = 0
def sol(s,t):
    if s == t :
        return 1
    if len(t) <= len(s):
        return 0
    if t and t[0] == 'B' and t[-1] == 'A':
        return sol(s,t[1:][::-1]) | sol(s,t[:-1])
    if t and t[0] == 'B':
        return sol(s,t[1:][::-1])
    if t and t[-1] == 'A':
        return sol(s,t[:-1])
    return 0
print(sol(S,T))