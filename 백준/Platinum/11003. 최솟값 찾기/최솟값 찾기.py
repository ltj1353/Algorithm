import sys
import heapq
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c = deque(list(map(int, input().rstrip().split())))
d = []
e = []

for i in range(a):
    heapq.heappush(e, (c.popleft(), i))
    if(i - b + 1 > 0):
        while(e[0][1] < i - b + 1):
            heapq.heappop(e)
    d.append(e[0][0])
print(*d)
