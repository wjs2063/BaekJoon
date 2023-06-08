import sys
input = sys.stdin.readline

n = int(input())

marbles = list(map(int,input().split()))

ans = 0

def backtracking(marbles,sub_ans):
    if len(marbles) == 2:
        global ans
        ans = max(ans,sub_ans)
        return

    for i in range(1,len(marbles) - 1):
        temp = marbles[i - 1] * marbles[i + 1]
        x = marbles.pop(i)
        backtracking(marbles,sub_ans + temp)
        marbles.insert(i,x)
backtracking(marbles,0)
print(ans)
