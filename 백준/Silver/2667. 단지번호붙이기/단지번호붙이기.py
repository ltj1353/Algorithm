import sys
from collections import deque
input = sys.stdin.readline

a = int(input().rstrip())
b = []

for i in range(a):
    b.append(list(map(int, input().rstrip())))

visited = [[0] * a for i in range(a)]
visit = deque()
ans = []

def bfs(b, i, j):
    count = 1
    visit.appendleft([i, j])
    visited[i][j] = 1
    while(visit):
        tmp = visit[-1]
        visit.pop()
        c = [[tmp[0], tmp[1] - 1], [tmp[0], tmp[1] + 1], [tmp[0] - 1, tmp[1]], [tmp[0] + 1, tmp[1]]]
        for k in c:
            if(k[0] >= 0 and k[0] < a and k[1] >= 0 and k[1] < a and b[k[0]][k[1]] == 1 and visited[k[0]][k[1]] == 0):
                visited[k[0]][k[1]] = 1
                count += 1
                visit.appendleft(k)
    return count
for i in range(a):
    for j in range(a):
        if(b[i][j] == 1 and visited[i][j] == 0):
            tmp = bfs(b, i, j)
            ans.append(tmp)
ans = sorted(ans)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
