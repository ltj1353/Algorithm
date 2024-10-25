import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(' '))
c = []
d = []
e = []
score = 0

for i in range(a):
    c.append(list(map(int, input().rstrip().split(' '))))

for k in range(a):
    ans = True
    d.clear()
    e.clear()
    for i in range(a):
        d.append(c[k][i])
        if(len(d) == 1):
            continue
        if(d[i - 1] == d[i]):
            continue
        elif(d[i - 1] > d[i]):
            if(a - len(d) < b - 1 or d[i - 1] - d[i] != 1):
                ans = False
                break
            for j in range(b):
                if(d[i] != c[k][i + j]):
                    ans = False
                    break
                e.append(i + j)
        else:
            if(len(d) > b):
                for j in range(b):
                    if(d[i - 1 - j] != d[i - 1] or i - 1 - j in e or d[i - 1] - d[i] != -1):
                        ans = False
                        break
            else:
                ans = False
                break
    if(ans == True):
        score += 1

for k in range(a):
    ans = True
    d.clear()
    e.clear()
    for i in range(a):
        d.append(c[i][k])
        if(len(d) == 1):
            continue
        if(d[i - 1] == d[i]):
            continue
        elif(d[i - 1] > d[i]):
            if(a - len(d) < b - 1 or d[i - 1] - d[i] != 1):
                ans = False
                break
            for j in range(b):
                if(d[i] != c[i + j][k]):
                    ans = False
                    break
                e.append(i + j)
        else:
            if(len(d) > b):
                for j in range(b):
                    if(d[i - 1 - j] != d[i - 1] or i - 1 - j in e or d[i - 1] - d[i] != -1):
                        ans = False
                        break
            else:
                ans = False
                break
    if(ans == True):
        score += 1
print(score)