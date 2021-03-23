
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
print(lev)
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
chlocks = [[fx,fy,1000]]
checkedposse=[]
i=0
while fx*fy > i:
    try:
        curr=chlocks.pop(0)
    except:
        break
    checkedposse.append(curr)
    if lev[curr[1]][curr[0]-1] == '0':
        lev[curr[1]][curr[0]-1] = curr[2]-1
        chlocks.append([curr[1],curr[0]-1,curr[2]-1])
    if lev[curr[1]-1][curr[0]] == '0':
        lev[curr[1]-1][curr[0]] = curr[2]-1
        chlocks.append([curr[1]-1,curr[0],curr[2]-1])
    if lev[curr[1]][curr[0]+1] == '0':
        lev[curr[1]][curr[0]+1] = curr[2]-1
        chlocks.append([curr[1],curr[0]+1,curr[2]-1])
    if lev[curr[1]+1][curr[0]] == '0':
        lev[curr[1]+1][curr[0]] = curr[2]-1
    i+=1
    #for i32 in lev:
    #    print(i32)
    #print(chlocks)
    #input()
    print(i)
#for i in lev:
#    print(i)
px,py=0,0
poves = []
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
        lev[py][px] = 'w'
        high = sorted(poves, key=lambda poves: poves[2])
        high = high[len(high)-1]
        px = high[0]
        py = high[1]
        if lev[py][px] == 1000:
            print("'AI' has found its way to the end!")
            exit()
        lev[py][px] = 'p'
    except Exception as e:
        print("Failed to find space!")
        print(str(e))
        exit()
    for i in lev:
        print(i)
    input()
