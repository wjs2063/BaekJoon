import sys
print(bin(int(sys.stdin.readline().strip()) + 1)[3:].replace("0","4").replace("1","7"))