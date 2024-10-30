import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split(' '))
d = [[] * (a + 1) for i in range(a + 1)]

start = 0
global visited
visited = [0] * (a + 1)

for i in range(b):
    e, f = map(int, input().rstrip().split(' '))
    d[e].append(f)
    d[f].append(e)

for i in range(1, a + 1):
    d[i] = sorted(d[i], reverse = True)

global count
count = 1
visit = deque()

def bfs(start):
    global count
    global visited
    visited[start] = count
    count += 1
    visit.appendleft(start)
    while(visit):
        tmp = visit[-1]
        visit.pop()
        for i in d[tmp]:
            if(visited[i] == 0):
                visited[i] = count
                count += 1
                visit.appendleft(i)
bfs(c)
for i in range(1, a + 1):
    sys.stdout.write(str(visited[i])+'\n')