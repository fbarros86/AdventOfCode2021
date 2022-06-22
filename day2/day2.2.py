hrz=0
dpt=0
aim=0
with open('input.txt','r') as f:
    for line in f.readlines():
        wds = line.split()
        n = int (wds[1])
        if (wds[0]=="forward"):
            hrz+=n
            dpt+=aim*n
        elif(wds[0]=="up"): aim-=n
        elif(wds[0]=="down"): aim+=n
print(str(hrz*dpt))
