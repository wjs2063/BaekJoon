import sys

sl,sr = input().strip().split()
left = {
    "q","w","e","r","t","a","s","d","f","g",
    "z","x","c","v"
}
alphabets = input().strip()

pos = {
    "z":(0,0),"x":(1,0),"c":(2,0),"v":(3,0),"b":(4,0),"n":(5,0),"m":(6,0),
    "a":(0,1),"s":(1,1),"d":(2,1),"f":(3,1),"g":(4,1),"h":(5,1),"j":(6,1),"k":(7,1),"l":(8,1),
    "q":(0,2),"w":(1,2),"e":(2,2),"r":(3,2),"t":(4,2),"y":(5,2),"u":(6,2),"i":(7,2),"o":(8,2),"p":(9,2)
}

time = 0
lx,ly = pos[sl]
rx,ry = pos[sr]
for alpha in alphabets:
    nx,ny = pos[alpha]
    if alpha in left:
        time += abs(nx - lx) + abs(ny - ly) + 1
        lx,ly = nx,ny
    else:
        time += abs(nx -rx) + abs(ny - ry) + 1
        rx,ry = nx,ny
print(time)
