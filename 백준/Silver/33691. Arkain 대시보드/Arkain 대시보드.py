import sys
input = sys.stdin.readline

a = int(input())
b = {}
for i in range(a):
    b[input().rstrip()] = i
c = int(input())
for i in range(c):
    b[input().rstrip()] += 100000

b = sorted(b.items(), key=lambda item: item[1], reverse = True)

for i in range(len(b)):
    print(b[i][0])
