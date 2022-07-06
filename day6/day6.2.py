
def getNFish (days, d):
    if (days<=0): return 1
    if (days not in d):
        d[days] = getNFish(days-7,d) + getNFish(days-9,d)
    return d[days]

d={}
r=0
with open('input.txt','r') as f:
    for n in f.readline().split(","):
        r+=getNFish(256-int(n),d)
print(str(r))
