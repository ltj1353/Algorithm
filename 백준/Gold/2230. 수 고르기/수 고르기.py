import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(' '))
c = []
start = 0
end = 1
score = 2000000000

for i in range(a):
    c.append(int(input().rstrip()))
c = sorted(c)

while(start < a - 1):
    if(c[end] - c[start] < b):
        if(end >= a - 1):
            start += 1
        else:
            end += 1
    else:
        # print(c[start],c[end])
        score = min(score, c[end] - c[start])
        start += 1
print(score)