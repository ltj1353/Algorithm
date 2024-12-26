import sys
from collections import deque
import random
input = sys.stdin.readline

a, b, c, d = map(int, input().rstrip().split(' '))
#a = random.randrange(1,10)
#b = random.randrange(1,40)
#c = random.randrange(0,b+1)
#d = random.randrange(1,100)

e = [[0, 0] for _ in range(a)]
f = []
g = []
h = {}
score = 0

for i in range(a):
    e[i][0], e[i][1] = map(int, input().rstrip().split(' '))
    h[e[i][0]] = i

e = sorted(e)
e.append([d, 0])
h[d] = a
e = e[::-1]
for i in e:
    while(f and f[-1][1] >= i[1]):
        f.pop()
    if(not f):
        f.append((i[0], i[1], 0, -1))
    else:
        f.append((i[0], i[1], f[-1][0], f[-1][1]))
    g.append(f[-1])
e = e[::-1]
g = g[::-1]
# print('tank',b,'fuel',c,'distance',d)
# print(g)

c -= g[0][0]
for station in range(a):
    if(c < 0):
        score = -1
        break
    dist = g[station][2] - g[station][0]
    cost = min(b, dist)
    # print(cost, c)
    if(cost > c):
        score += (cost - c) * g[station][1]
        c = cost
    c -= g[station + 1][0] - g[station][0]
    # print('fuel',c)
    # print('score',score)
print(score)

