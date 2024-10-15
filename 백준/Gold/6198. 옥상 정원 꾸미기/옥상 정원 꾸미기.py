import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = []
c = []
d = [0] * a
score = 0

for i in range(a):
    b.append((int(input().rstrip()), i))

for i in b:
    while(c and i[0] >= c[-1][0]):
        d[c[-1][1]] = i[1] - c[-1][1] - 1
        c.pop()
    c.append((i[0], i[1]))

for i in range(len(c)):
    d[c[i][1]] = a - c[i][1] - 1

for i in d:
    score += i
    
print(score)