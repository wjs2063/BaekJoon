import sys
input = sys.stdin.readline
h,w = map(int,input().split())

graph = []

for _ in range(h):
    graph.append(input().strip())

# 어떻게 효과적으로 내부영역을 판단할것인가?
# 결국 폐쇄된 도형이기 떄문에 수평선을 그어보면 / 나 \ 를 만나게 되어있다.
# 반복문 돌리면서 / 를 만나면 stack 에 넣고 / 나 \ 를 만나면 제거 도중에 . 을만나면 + 1
stack = []
area = 0
for i in range(h):
    for j in range(w):
        # stack 에 뭐가 들어있는경우
        if stack :
            if graph[i][j] == '.':
                area += 1
            else:
                area += 0.5
                stack.pop()
        # stack 에 뭐가 들어있지않은경우
        else:
            # / 나 \ 만 넣고 +0.5
            if graph[i][j] in ['/','\\']:
                area += 0.5
                stack.append(graph[i][j])
print(int(area))
