import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c = list(map(int, input().rstrip().split()))
d = [0] * b
e = {}
f = [1] * b
score = 0

if(len(c) > 1):
    for i in range(1, len(c)):
        e[c[i]] = 1

for i in range(b):
    d[i] = (list(map(int, input().rstrip().split())))

for _ in range(b):
    for i in range(b):
        for j in range(1, len(d[i])):
            if(d[i][j] in e):
                f[i] = 0
                for k in range(1, len(d[i])):
                    e[d[i][k]] = 1
                break

for i in f:
    if(i == 1):
        score += 1

# print(e)
# print(f)
print(score)
