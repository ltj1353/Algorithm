import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = []
c = []
score = 0
ans = []

for i in range(a):
    b.append(((int(input().rstrip())), i))
b.append((-1, a))
# print(b)

for i in b:
    while(c and c[-1][0] >= i[0]):
        score = max(score, c[-1][0] * (i[1] - c[-1][3] - 1))
        # print(f'{c[-1][0]}*{i[1] - c[-1][3] - 1}={c[-1][0] * (i[1] - c[-1][3] - 1)}')
        c.pop()
    if(not c):
        score = max(score, i[0])
        c.append((i[0], i[1], 0, -1))
    else:
        score = max(score, i[0])
        c.append((i[0], i[1], c[-1][0], c[-1][1]))
    # print(c)
print(score)