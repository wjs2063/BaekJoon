import sys
input = sys.stdin.readline


n = int(input())
k = int(input())


sensor = list(map(int,input().split()))

sensor.sort()
n = len(sensor)
diff = []
for i in range(1,n):
    diff.append(sensor[i] - sensor[i - 1])
diff.sort()

if k - 1 >= len(diff):
    print(0)
else:
    print(sum(diff[:len(diff) - (k - 1)]))

