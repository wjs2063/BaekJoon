import sys
input = sys.stdin.readline

board = input().strip()

n = len(board)
cnt = 0
ans = ""
for i in range(n):
    if board[i] != ".":
        cnt += 1
    if board[i] == ".":
        q,r = divmod(cnt,2)
        if r == 1:
            ans = -1
            break
        ans += "AAAA"*(q // 2)
        ans += "BB"*(q - 2*(q // 2))
        ans += "."
        cnt = 0
if cnt > 0:
    q,r = divmod(cnt,2)
    if r == 1:
        ans = -1
    else:
        ans += "AAAA"*(q // 2)
        ans += "BB" * (q - 2*(q // 2))
print(ans)
