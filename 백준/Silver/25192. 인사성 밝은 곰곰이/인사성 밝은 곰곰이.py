import sys
input = sys.stdin.readline


a = int(input().rstrip())
b = []
c = {}
score = 0

for i in range(a):
    b.append(input().rstrip())

for i in b:
    if(i == "ENTER"):
        score += len(c)
        c = {}
    else:
        if(i not in c):
            c[i] = 1
score += len(c)

print(score)