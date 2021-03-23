\
lev=[]
with open('map.txt') as f:
    for line in f:
        tmp=[]
        for letter in line:
            if letter != '\n':
                tmp.append(letter.replace('.', '0'))
        lev.append(tmp)
ly=len(lev)
lx=len(lev[0])
for i in lev:
    print(i)
fx=0
fy=0
for line in lev:
    try:
        fx = line.index('x')
        break
    except:
        pass
    fy+=1
print(fx,fy)
lev[fy][fx] = 1000
i=0
poves = []
check = [[fx,fy,1000]]
ox,oy=fx,fy
while ox*oy*2 > i:
    for curr in check:
        poves=[]
        fx,fy = curr[0], curr[1]
        if not lev[fy][fx+1] == 'w' and not type(lev[fy][fx+1]) == int:
            poves.append((fx+1, fy, int(lev[fy][fx+1])))
        if not lev[fy][fx-1] == 'w' and not type(lev[fy][fx-1]) == int:
            poves.append((fx-1, fy, int(lev[fy][fx-1])))
        if not lev[fy+1][fx] == 'w' and not type(lev[fy+1][fx]) == int:
            poves.append((fx, fy+1, int(lev[fy+1][fx])))
        if not lev[fy-1][fx] == 'w' and not type(lev[fy-1][fx]) == int:
            poves.append((fx, fy-1, int(lev[fy-1][fx])))
        print(poves)
        for ords in poves:
            lev[ords[1]][ords[0]] = lev[fy][fx] - 1
        try:
            check.append([poves[len(poves)-1][0],poves[len(poves)-1][1]])
        except:
            check.append([poves[0][0],poves[0][1]])
    i+=1
    print(i)
px,py=0,0
poves = []
n=0
for line in lev:
    try:
        px = line.index('p')
        break
    except:
        pass
    py+=1
while True:
    poves=[]
    print(px,py)
    try:
        if not lev[py][px+1] == 'w':
            poves.append((px+1, py, int(lev[py][px+1])))
        if not lev[py][px-1] == 'w':
            poves.append((px-1, py, int(lev[py][px-1])))
        if not lev[py+1][px] == 'w':
            poves.append((px, py+1, int(lev[py+1][px])))
        if not lev[py-1][px] == 'w':
            poves.append((px, py-1, int(lev[py-1][px])))
        high = sorted(poves, key=lambda poves: poves[2])
        high = high[len(high)-1]
        lev[py][px] = -1-n
        px = high[0]
        py = high[1]
        if lev[py][px] == 1000:
            print("'AI' has found its way to the end!")
            exit()
        lev[py][px] = 'p'
        n+=1
    except Exception as e:
        print("Failed to find space!")
        print(str(e))
        exit()
    for i in lev:
        print(i)
    input()
