''' https://adventofcode.com/2021/day/1 '''

x1 = int(input())
x2 = int(input())
x3 = int(input())
t1 = x1+x2+x3
r=0
while (x3!=10526):
    x4 = int(input())
    t2 = t1-x1+x4
    if (t2>t1): r+=1
    x1=x2
    x2=x3
    x3=x4
    t1=t2
r=str(r)
print("Valor:"+r)
