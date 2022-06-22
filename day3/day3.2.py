def getOxygen (list, i):
    if (len(list)==1): return list[0]
    zeros=[]
    ones = []
    for line in list:
        if (line[i]=='0'): zeros.append(line)
        elif (line[i]=='1'): ones.append(line)
    if (len(zeros)>len(ones)): return getOxygen(zeros,i+1)
    else: return getOxygen(ones,i+1)

def getCO2 (list, i):
    if (len(list)==1): return list[0]
    zeros=[]
    ones = []
    for line in list:
        if (line[i]=='0'): zeros.append(line)
        elif (line[i]=='1'): ones.append(line)
    if (len(zeros)<=len(ones)): return getCO2(zeros,i+1)
    else: return getCO2(ones,i+1)

def binToDec (nbin):
    r=0
    size=len(nbin)-1
    for i in range(0,size):
        if (nbin[i]=='1'): r+=pow(2,(size-i-1))
    return r

zeros=[]
ones = []
with open('input.txt','r') as f:
    for line in f.readlines():
        if (line[0]=='0'): zeros.append(line)
        elif (line[0]=='1'): ones.append(line)
if (len(zeros)>len(ones)):
    ox = getOxygen(zeros,1)
    co2 = getCO2(ones,1)
else:
    ox = getOxygen(ones,1)
    co2 = getCO2(zeros,1)
print(str(binToDec(ox)))
print(str(binToDec(co2)))
print(str(binToDec(ox)*binToDec(co2)))
