hrz=0
dpt=0
with open('input.txt','r') as f:
    for line in f.readlines():
        wds = line.split()
        n = int (wds[1])
        if (wds[0]=="forward"): hrz+=n
        elif(wds[0]=="up"): dpt-=n
        elif(wds[0]=="down"): dpt+=n
print(str(hrz*dpt))
