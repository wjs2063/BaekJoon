import sys
input = sys.stdin.readline

n = int(input().strip())
# back tracking


# check 함수 : 문자열이 좋은수열인지 나쁜수열인지 확인해주는 함수 (좋은문자열이면 True 반환)
def is_good(string):
    # 이어져있는 두 문자가 같은지 확인
    # 길이 1짜리, 2짜리 3짜리 . . . len(string) // 2 짜리 다확인
    for term in range(1,len(string) // 2 + 1):
        # term 에 대해서 길이 모두 확인
        for i in range(len(string) - term + 1):
            if string[i:i + term] == string[i + term:i + 2*term]:
                return False
    return True

flag = True
def dfs(string,distance,n):
    # 현재 문자열 string, 길이 distance
    # 종료조건
    global flag
    if distance == n:
        print(string)
        flag = False
        return
    words = ["1","2","3"]
    for word in words:
        if is_good(string + word) and flag:
            dfs(string + word,distance + 1,n)
dfs("1",1,n)