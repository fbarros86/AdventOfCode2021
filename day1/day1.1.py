''' https://adventofcode.com/2021/day/1 '''

x = int(input())
r=0
while (x!=10526):
    y = int(input())
    if (y>x): r+=1
    x=y
r=str(r)
print("Valor:"+r)
