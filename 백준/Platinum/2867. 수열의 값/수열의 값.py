import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = []
c = []
d = []

acount = 0
bcount = 0
mini = 0
maxi = 0
score = 0

for i in range(a):
    b.append([int(input().rstrip()), 1])

for i in b:
    while(c and c[-1][0] < i[0]):
        acount += c[-1][1]
        maxi -= c[-1][0] * c[-1][1]
        c.pop()
    c.append([i[0], 1])
    while(d and d[-1][0] > i[0]):
        bcount += d[-1][1]
        mini -= d[-1][0] * d[-1][1]
        d.pop()
    d.append([i[0], 1])

    c[-1][1] += acount
    d[-1][1] += bcount

    maxi += (c[-1][1] * c[-1][0])
    mini += (d[-1][1] * d[-1][0])
    acount = 0
    bcount = 0
    score += maxi
    score -= mini
    # print('max',maxi)
    # print('min',mini)

print(score)