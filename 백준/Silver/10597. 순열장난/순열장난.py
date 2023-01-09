import sys
input = sys.stdin.readline

s = input().strip()
# 배열담고
answer = []
path = set()
flag = True

# backtracking 1칸전진 or 2칸전진 모두 진행
def dfs(answer,path,idx,s):
    global flag
    # 언제 종료?
    # max(answer) 이 곧 n 인데 1부터 n 까지 다있는지 확인해야함 길이와 max값이 같으면 가능
    if idx >= len(s) and len(answer) == max(answer):
        flag = False
        print(*answer)
        return
    # 1부터 50 까지만 가능함
    # 1칸 갈수있는경우 -> 인덱스가 범위안에있으며 && 숫자또한 1자리 숫자이면서 && 이전에 쓴 숫자가 아니고 && 이미 답을 구한상태가아닌경우
    if idx < len(s) and 1 <= int(s[idx]) < 10 and int(s[idx]) not in path and flag:
        dfs(answer + [int(s[idx])],path | {int(s[idx])},idx + 1,s)
    # 2칸갈수있는경우 현재 idx 와 idx + 1 칸이 정상 인덱스범위안에있으면 가능, 그리고 숫자가 2자리범위, 이전에 쓴 숫자아니고 , 답 구하지않은경우
    if idx + 1 < len(s) and 10 <= int(s[idx:idx + 2]) <= 50 and int(s[idx : idx + 2]) not in path and flag:
        dfs(answer + [int(s[idx : idx + 2])] , path | {int(s[idx : idx + 2])}, idx + 2,s)

dfs(answer,set(),0,s)


"""
67891054321

6 7 8 9 10 5 4 3 2 1

"""