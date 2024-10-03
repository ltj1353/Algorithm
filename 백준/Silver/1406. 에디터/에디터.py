import sys
a=list(sys.stdin.readline().rstrip())
b=[]
d=int(input())

for _ in range(d):
    c = sys.stdin.readline().rstrip().split()
    if c[0]=='L' and len(a) > 0:
        b.append(a.pop())
    elif c[0]=='D' and 0 < len(b):
        a.append(b.pop())
    elif c[0]=='B' and len(a) > 0:
        a.pop()
    elif c[0]=='P':
        a.append(c[1])
b.reverse()
print("".join((a+b)))
