with open('input.txt','r') as f:
    size = None
    counter={}
    for line in f.readlines():
        if (not size):
            size = len(line)-1
            for i in range(0,size): counter[i]=0
        for i in range(0,size):
            if (line[i]=='0'): counter[i]-=1
            elif (line[i]=='1'): counter[i]+=1
gamma=0
epsilon=0
for i in range(0,size):
    if (counter[i]>0): gamma += pow(2,(size-i-1))
    else: epsilon += pow(2,(size-i-1))
print(str(gamma*epsilon))
