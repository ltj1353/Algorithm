import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split(' '))
d = [[] * (a + 1) for i in range(a + 1)]
visit = deque()

for i in range(b):
    e, f = map(int, input().rstrip().split(' '))
    d[e].append(f)
    d[f].append(e)

for i in range(1, a + 1):
    d[i] = sorted(d[i])

def dfs(start):
    global count
    visited[start] = 1
    count.append(start)
    for i in d[start]:
        if(visited[i] == 0):
            dfs(i)

def bfs(start):
    global count
    visited[start] = 1
    count.append(start)
    visit.appendleft(start)
    while(visit):
        tmp = visit[-1]
        visit.pop()
        for i in d[tmp]:
            if(visited[i] == 0):
                visited[i] = 1
                count.append(i)
                visit.appendleft(i)

global count
count = []
visited = [0] * (a + 1)
dfs(c)
print(*count)

count = []
visited = [0] * (a + 1)
bfs(c)
print(*count)
