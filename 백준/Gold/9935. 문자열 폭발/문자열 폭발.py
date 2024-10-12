import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = []

for i in a:
    c.append(i)
    if(len(c) >= len(b)):
        if("".join(c[-(len(b)):]) == b):
            for _ in range(len(b)):
                c.pop()

if(c):
    print("".join(c))
else:
    print('FRULA')
