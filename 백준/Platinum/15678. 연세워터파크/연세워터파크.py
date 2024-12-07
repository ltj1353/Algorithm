import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(" "))
c = list(map(int, input().rstrip().split(" ")))
d = deque()
score = max(c)

d.append((0, 0))
for i in range(a):
    k = c[i]

    while(d and d[0][1] + b < i):
        d.popleft()

    tmp = max(k, k + d[0][0])
    score = max(score, tmp)

    while(d and d[-1][0] <= tmp):
        d.pop()

    d.append((tmp, i))
print(score)