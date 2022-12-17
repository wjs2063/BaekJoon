import sys

input = sys.stdin.readline

ip = input().rstrip()

if "::" in ip :
    xx = ip.split("::")
    if xx[0] != '' and xx[-1] == '':
        x = xx[0].split(":")
        for _ in range(8 - len(x)):
            x.append("0")
    elif xx[0] != '' and xx[-1] != '':
        lx = xx[0].split(":")
        ly = xx[-1].split(":")
        x = lx + ['0'] * ( 8 - len(lx) - len(ly)) + ly
    elif xx[0] == '' and xx[-1] != '':
        ly = xx[-1].split(":")
        x = ['0']*(8 - len(ly)) + ly
    else :
        x = ['0'] * 8
    for i in range(8):
        x[i] = x[i].zfill(4)
    print(":".join(x))
else:
    ip = ip.split(':')
    for i in range(8):
        ip[i] = ip[i].zfill(4)
    print(":".join(ip))



