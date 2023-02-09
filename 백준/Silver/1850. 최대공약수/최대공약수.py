import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def gcd(a,b):
    while b > 0 :
        a,b = b, a % b
    return a

print("1"*gcd(a,b))
