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
check = [[fx,fy]]
ox,oy=fx,fy
xindex,yindex=0,0
while ox*oy > i:
    for asdf in check:
        fx,fy = asdf[0], asdf[1]
        poves = []
        coords = [[fy,fx+1,lev[fy][fx]], [fy,fx-1,lev[fy][fx]], [fy+1,fx,lev[fy][fx]], [fy-1,fx,lev[fy][fx]]]
        for it in coords:
            coord = lev[it[0]][it[1]]
            if not coord == 'w' and not coord == 'p' and not type(coord) == int:
                poves.append(it)
        for it in poves:
            lev[it[0]][it[1]] = int(lev[fy][fx])-1
            check.append([it[1], it[0]])
    i+=1
'''for line in lev:
    xindex=0
    print(yindex, xindex)
    for coord in line: 
        if not coord == 'w' and not coord == 'p' and not type(coord) == int:
            lev[yindex][xindex] = (1000-(fy-yindex))-(fx-xindex)
        xindex+=1
    yindex+=1
    for i in lev:
        print(i)    
''' #add as fallback code if main method fails?
px,py=0,0
poves = []
n=0
for i in lev:
    print(i)
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
