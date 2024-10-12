import sys
input = sys.stdin.readline

a, b = map(int,input().rstrip().split(' '))
c = {}

for i in range(a):
    d = input().rstrip()
    if(len(d) < b):
        continue
    elif(d not in c):
        c[d] = 1
    else:
        c[d] = c[d] + 1

e = sorted(c.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
for i in range(len(e)):
    print(e[i][0])