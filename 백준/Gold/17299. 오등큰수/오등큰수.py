import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = list(map(int, input().rstrip().split()))
c = []
d = {}
e = []
f = []
count = 0

for i in b:
    if(i not in d):
        d[i] = 1
    else:
        d[i] += 1

for i in b:
    c.append((d[i], i, count))
    count += 1

# print(c)
c = reversed(c)


for i in c:
    while(e and e[-1][0] <= i[0]):
        e.pop()
    if(not e):
        e.append((i[0], -1, i[1]))
        f.append(-1)
    elif(e[-1][0] > i[0]):
        f.append(e[-1][2])
        e.append((i[0], e[-1][0], i[1]))
    # print(e,f)
f = reversed(f)
print(*f)
