import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(' '))
c = []

for i in range(a):
    c.append(list(map(int, input().rstrip().split(' '))))

ans = []

def bfs(c, i, j):
    visit = deque()
    visited = [[-1] * b for i in range(a)]
    visit.appendleft([i, j])
    visited[i][j] = 0
    while(visit):
        tmp = visit[-1]
        visit.pop()
        d = [[tmp[0], tmp[1] - 1], [tmp[0], tmp[1] + 1], [tmp[0] - 1, tmp[1]], [tmp[0] + 1, tmp[1]], [tmp[0] - 1, tmp[1] - 1], [tmp[0] - 1, tmp[1] + 1], [tmp[0] + 1, tmp[1] - 1], [tmp[0] + 1, tmp[1] + 1]]
        for k in d:
            if(k[0] < 0 or k[0] >= a or k[1] < 0 or k[1] >= b):
                continue
            if(c[k[0]][k[1]] == 0 and visited[k[0]][k[1]] == -1):
                visited[k[0]][k[1]] = visited[tmp[0]][tmp[1]] + 1
                visit.appendleft(k)
            if(c[k[0]][k[1]] == 1 and visited[k[0]][k[1]] == -1):
                return visited[tmp[0]][tmp[1]] + 1
    return visited[tmp[0]][tmp[1]]
for i in range(a):
    for j in range(b):
        if(c[i][j] == 0):
            tmp = bfs(c, i, j)
            ans.append(tmp)

if(None in ans):
    print(0)
else:
    print(max(ans))
