import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split(' '))
d = [[] * (a + 1) for i in range(a + 1)]

start = 0
visited = [0] * (a + 1)

for i in range(b):
    e, f = map(int, input().rstrip().split(' '))
    # d[e][f] = 1
    # d[f][e] = 1
    d[e].append(f)
    d[f].append(e)

# for i in range(a + 1):
#     for j in range(a + 1):
#         print(d[i][j], end='')
#     print()

global count
count = 1

def dfs(start):
    global count
    visited[start] = count
    count += 1

    for i in sorted(d[start]):
        if(visited[i] == 0):
            dfs(i)
dfs(c)
for i in range(1, a + 1):
    sys.stdout.write(str(visited[i])+'\n')