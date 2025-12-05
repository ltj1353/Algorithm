import sys
input = sys.stdin.readline

a = int(input())
b = [[0, 0]] + [list(map(int, input().split())) for _ in range(a)]

c = [0] * (a + 2)

for i in range(a, 0, -1):
    t = b[i][0]
    p = b[i][1]
    f = i + t
    if f > a + 1:
        c[i] = c[i + 1]
    else:
        c[i] = max(c[i + 1], p + c[f])

print(c[1])
