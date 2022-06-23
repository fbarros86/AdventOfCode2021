

map={}
r=0
with open('input.txt','r') as f:
    for line in f.readlines():
        words = line.split()
        p1 = words[0].split(",")
        p2 = words[2].split(",")
        x1= min(int(p1[0]),int(p2[0]))
        x2= max(int(p1[0]),int(p2[0]))
        y1= min(int(p1[1]),int(p2[1]))
        y2= max(int(p1[1]),int(p2[1]))
        if (x1==x2 or y1==y2):
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if ((x,y) not in map): map[(x,y)]=1
                    elif(map[(x,y)]==1):
                        map[(x,y)]=2
                        r+=1
print(str(r))
