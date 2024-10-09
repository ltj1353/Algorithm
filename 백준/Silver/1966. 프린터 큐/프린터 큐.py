import sys
from collections import deque
input = sys.stdin.readline

a = int(input())

for i in range(a):
    n, m = map(int,input().split())
    b = deque(map(int,input().split()))
    c = m
    score = 0
    while (True):
        if (b[0] < max(b)):
            b.append(b.popleft())
        else:
            b.popleft()
            score += 1
            if (c == 0):
                print(score)
                break
        if (c == 0):
            c = len(b)
        c -= 1
