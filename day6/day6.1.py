
currFish = []
with open('input.txt','r') as f:
    for n in f.readline().split(","):
        currFish.append(int(n))
d=1
while (d<257):
    newFish=[]
    for f in currFish:
        if (not f):
            newFish.append(6)
            newFish.append(8)
        else: newFish.append(f-1)
    currFish=newFish
    d+=1
print(str(len(currFish)))
