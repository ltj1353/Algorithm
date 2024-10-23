import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = []
mini = [[0] * 3 for i in range(2)]
maxi = [[0] * 3 for i in range(2)]

for i in range(a):
    b.append(list(map(int, input().rstrip().split(' '))))

i = 0
j = 1

for k in range(a):
    mini[i][0] += min(mini[j][0], mini[j][1]) + b[k][0]
    mini[i][1] += min(mini[j][0], mini[j][1], mini[j][2]) + b[k][1]
    mini[i][2] += min(mini[j][1], mini[j][2]) + b[k][2]

    maxi[i][0] += max(maxi[j][0], maxi[j][1]) + b[k][0]
    maxi[i][1] += max(maxi[j][0], maxi[j][1], maxi[j][2]) + b[k][1]
    maxi[i][2] += max(maxi[j][1], maxi[j][2]) + b[k][2]
    tmp = i
    i = j
    j = tmp
    if(k % 2 == 0):
        mini[i] = [0, 0, 0]
        maxi[i] = [0, 0, 0]
    else:
        mini[i] = [0, 0, 0]
        maxi[i] = [0, 0, 0]
    # print(mini)
    # print(maxi)
    # print(b[k])
if(a % 2 == 1):
    print(max(maxi[0]), min(mini[0]))
else:
    print(max(maxi[1]), min(mini[1]))
