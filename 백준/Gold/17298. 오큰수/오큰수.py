import sys
input = sys.stdin.readline
a = input().rstrip()
b = list(map(int,input().rstrip().split()))
c = []
d = []
b = reversed(b)
for i in b:
    while(c and c[-1][0] <= i):
        c.pop()
    if(not c):
        c.append((i,-1))
    else:
        c.append((i,c[-1][0]))
    d.append(c[-1][1])
d = d[::-1]
print(*d)
    
