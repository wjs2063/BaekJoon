def solution(n):
    def check(x):
        if x == 2 :return 1
        for i in range(2,int(x ** 0.5) + 1):
            if x % i == 0 :return 0
        return 1
    ans = 0
    for i in range(2,n + 1):
        if check(i):
            ans += 1
        
    return ans