import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = [[] * (a + 1) for i in range(a + 1)]

for i in range(b):
    d, e = map(int, input().rstrip().split())
    c[d].append(e)
    c[e].append(d)

global count
count = -1
visited = [0] * (a + 1)

def dfs(start):
    global count
    for i in c[start]:
        if(visited[i] == 0):
            count += 1
            visited[i] = 1
            dfs(i)
dfs(1)
if(count == -1):
    print(0)
else:
    print(count)