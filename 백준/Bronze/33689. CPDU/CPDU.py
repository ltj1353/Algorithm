import sys
input = sys.stdin.readline

a = int(input())
b = []
c = 0

for i in range(a):
    b.append(input())
    if(b[i][0] == "C"):
        c += 1

print(c)